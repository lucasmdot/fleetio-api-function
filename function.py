import requests
import json

def create_work_order(extracted_data):

    url = "https://secure.fleetio.com/api/v2/work_orders"

    payload = json.dumps({
    "issued_at": "2023-03-14T13:46:27-06:00",
    "started_at": "2023-03-14T13:46:27-06:00",
    "completed_at": extracted_data['date_of_service'], # format: 2023-03-14T13:46:27-06:00
    "work_order_status_id": 0,
    "invoice_number": "string",
    "vendor_id": 0,
    "vendor_name": "string", # extracted_data['name']
    "vehicle_id": 0,
    "vehicle_name": "string",
    "discount_type": "percentage",
    "discount": 0,
    "discount_percentage": 0,
    "parts_markup_percentage": 0,
    "parts_markup_type": "percentage",
    "parts_markup": 0,
    "labor_markup_percentage": 0,
    "labor_markup_type": "percentage",
    "labor_markup": 0,
    "tax_1_percentage": 0,
    "tax_1_type": "percentage",
    "tax_1": 0,
    "tax_2_percentage": 0,
    "tax_2_type": "percentage",
    "tax_2": 0,
    "issued_by_id": 0,
    "contact_id": 0,
    "label_list": "High Priority",
    "purchase_order_number": "string",
    "description": extracted_data['work_done'],
    "number": 0,
    "meter_entry_attributes": {
        "value": "108043",
        "void": True
    },
    "secondary_meter_entry_attributes": {
        "value": "108043",
        "void": True
    },
    "starting_meter_entry_attributes": {
        "value": "108043",
        "void": True
    },
    "ending_meter_entry_attributes": {
        "value": "108043",
        "void": True
    },
    "starting_secondary_meter_entry_attributes": {
        "value": "108043",
        "void": True
    },
    "ending_secondary_meter_entry_attributes": {
        "value": "108043",
        "void": True
    },
    "custom_fields": {},
    "ending_meter_same_as_start": True,
    "vmrs_repair_priority_class_id": 0,
    "scheduled_at": "2025-03-13",
    "expected_completed_at": "2025-03-13",
    "comments_attributes": [
        {
        "title": "string",
        "comment": "string"
        }
    ],
    "work_order_line_items_attributes": [
        {
        "id": 0,
        "item_type": "Issue",
        "item_name": "string",
        "description": "string",
        "item_id": 0,
        "labor_cost": 0,
        "parts_cost": 0,
        "position": 0,
        "subtotal": int(extracted_data['cost']), # extracted_data['cost']
        "type": "WorkOrderServiceTaskLineItem",
        "vmrs_reason_for_repair_id": 0,
        "vmrs_system_group_id": 0,
        "vmrs_system_id": 0,
        "vmrs_assembly_id": 0,
        "vmrs_component_id": 0,
        "issue_ids": [
            0
        ],
        "work_order_sub_line_items_attributes": [
            {
            "id": 0,
            "type": "WorkOrderPartLineItem",
            "item_id": 0,
            "item_type": "Part",
            "quantity": 0,
            "part_location_detail_id": 0,
            "position": 0,
            "description": "string",
            "inventory_set_id": 0,
            "vmrs_reason_for_repair_id": 0,
            "vmrs_system_group_id": 0,
            "vmrs_system_id": 0,
            "vmrs_assembly_id": 0,
            "vmrs_component_id": 0,
            "labor_time_entries_attributes": [
                {
                "started_at": "2025-03-13",
                "ended_at": "2025-03-13",
                "contact_id": 0
                }
            ]
            }
        ],
        "work_order_part_line_items_attributes": [
            {
            "id": 0,
            "type": "WorkOrderPartLineItem",
            "item_id": 0,
            "item_type": "Part",
            "quantity": 0,
            "part_location_detail_id": 0,
            "position": 0,
            "description": "string",
            "inventory_set_id": 0,
            "vmrs_reason_for_repair_id": 0,
            "vmrs_system_group_id": 0,
            "vmrs_system_id": 0,
            "vmrs_assembly_id": 0,
            "vmrs_component_id": 0,
            "labor_time_entries_attributes": [
                {
                "started_at": "2025-03-13",
                "ended_at": "2025-03-13",
                "contact_id": 0
                }
            ]
            }
        ],
        "work_order_labor_line_items_attributes": [
            {
            "id": 0,
            "type": "WorkOrderPartLineItem",
            "item_id": 0,
            "item_type": "Part",
            "quantity": 0,
            "part_location_detail_id": 0,
            "position": 0,
            "description": "string",
            "inventory_set_id": 0,
            "vmrs_reason_for_repair_id": 0,
            "vmrs_system_group_id": 0,
            "vmrs_system_id": 0,
            "vmrs_assembly_id": 0,
            "vmrs_component_id": 0,
            "labor_time_entries_attributes": [
                {
                "started_at": "2025-03-13",
                "ended_at": "2025-03-13",
                "contact_id": 0
                }
            ]
            }
        ]
        }
    ],
    "work_order_sub_line_items_attributes": [
        {
        "id": 0,
        "type": "WorkOrderPartLineItem",
        "item_id": 0,
        "item_type": "Part",
        "quantity": 0,
        "part_location_detail_id": 0,
        "position": 0,
        "description": "string",
        "inventory_set_id": 0,
        "vmrs_reason_for_repair_id": 0,
        "vmrs_system_group_id": 0,
        "vmrs_system_id": 0,
        "vmrs_assembly_id": 0,
        "vmrs_component_id": 0,
        "labor_time_entries_attributes": [
            {
            "started_at": "2025-03-13",
            "ended_at": "2025-03-13",
            "contact_id": 0
            }
        ]
        }
    ],
    "issue_ids": [
        0
    ],
    "label_ids": [
        0
    ],
    "documents_attributes": [
        {
        "name": "string",
        "file_url": "string",
        "file_mime_type": "string",
        "file_name": "string",
        "file_size": 0
        }
    ],
    "images_attributes": [
        {
        "name": "string",
        "file_url": "string",
        "file_mime_type": "string",
        "file_name": "string",
        "file_size": 0
        }
    ]
    })
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Token INSERT_TOKEN_HERE',
    'Account-Token': 'INSERT_ACCOUNT_TOKEN',
    'X-Api-Version': '2024-06-30'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)