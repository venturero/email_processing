import re
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=(os.getenv('OPENAI_API_KEY')))

def extract_order_details(email_text):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an order extraction assistant. Extract the product name and exact quantity from emails. Respond with 'Product: [product name], Quantity: [number]'. If no quantity is specified, default to 1."},
                {"role": "user", "content": f"Extract the product name and quantity from this email: {email_text}"}
            ],
            max_tokens=150
        )
        
        extracted_text = response.choices[0].message.content.strip()
        
        product_match = re.search(r'Product:\s*([\w\s]+)', extracted_text)
        quantity_match = re.search(r'Quantity:\s*(\d+)', extracted_text)

        product = product_match.group(1).strip() if product_match else "Unknown Product"
        quantity = quantity_match.group(1).strip() if quantity_match else "1"

        return {
            'product': product,
            'quantity': int(quantity)  
        }
    
    except Exception as e:
        print(f"Error extracting order details: {e}")
        return {
            'product': "Unknown Product",
            'quantity': 1
        }
