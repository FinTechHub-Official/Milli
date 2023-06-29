from django.db import connection
from collections import defaultdict
from api.v1.product.models import Category
import time, requests


def get_all_active_category():
    query = """
        SELECT c1.id, c1.title_ln,
            c2.id AS children_id, c2.title_ln AS children_title_ln,
            c3.id AS sub_children_id, c3.title_ln AS sub_children_title_ln
        FROM product_category c1
        LEFT JOIN product_category c2 ON c1.id = c2.parent_id
        LEFT JOIN product_category c3 ON c2.id = c3.parent_id
        WHERE c1.parent_id IS NULL and c1.is_active = true and c1.is_deleted = false;
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        results = defaultdict(lambda: {
            "id": None,
            "title": None,
            "children": []
        })
        for row in cursor.fetchall():
            parent_id, title, child_id, child_title, sub_child_id, sub_child_title = row[:6]
            parent = results[parent_id]
            parent['id'] = parent_id
            parent['title'] = title
            child = next((c for c in parent['children'] if c['id'] == child_id), None)
            if not child:
                child = {
                    "id": child_id,
                    "title": child_title,
                    "children": []
                }
                parent['children'].append(child)

            sub_child = {
                "id": sub_child_id,
                "title": sub_child_title,
                "children": []
            }
            child['children'].append(sub_child)
    return list(results.values())


# GET UZUM.UZ CATEGORIES
def get_categories():
    url = 'https://api.uzum.uz/api/main/root-categories?eco=false'
    headers = {
        "Authorization": "Basic YjJjLWZyb250OmNsaWVudFNlY3JldA==",
        "Accept-Language": "uz-UZ"
    }
    response = requests.get(url, headers=headers)
    return response.json()['payload']

def save_categories():
    categories = get_categories()
    son = 1
    for category in categories:
        category_obj = Category(
            title_ln=category.get("title")
        )
        category_obj.save()
        time.sleep(3)
        if category.get("children"):
            for category_child in category.get("children"):
                category_child_obj = Category(
                    title_ln=category_child.get("title"),
                    parent_id=category_obj.id
                )
                category_child_obj.save()
                time.sleep(3)
                if category_child.get("children"):
                    category_child_objs = [
                        Category(
                            title_ln=category_child_child.get('title'),
                            parent_id=category_child_obj.id
                        ) for category_child_child in category_child.get("children")
                    ]
                    if category_child_objs:
                        Category.objects.bulk_create(category_child_objs)
                print(son)
                son+=1
