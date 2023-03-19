import json

def lambda_handler(event, context):
    # Extract name from event payload
    name = event['name']

    # Construct greeting message
    message = f"Hello, {name}!"

    # Return response with status code based on name value
    if name == "Alice":
        response = {
            'statusCode': 200,
            'body': json.dumps(message)
        }
    elif name == "Bob":
        response = {
            'statusCode': 202,
            'body': json.dumps(message)
        }
    else:
        response = {
            'statusCode': 400,
            'body': json.dumps("Invalid name")
        }

    return response
