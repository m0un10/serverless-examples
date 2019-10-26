# General Notes

- Make sure to use `personal` AWS profile or update `profile: ` in `serverless.yml`.

# File Structure Explained

| Component | Description |
| --------- | ----------- |
| libs | Common components for DynamoDb and Cors/Response builder |
| mocks | Payloads for testing each event |
| resources | Cloudformation used by Serverless Framework |
| create.js | Create Note |
| delete.js | Delete Note |
| get.js | Get Note |
| list.js | List Note |
| update.js | Update Note |
| serverless.yml | Serverless Framework Definition |

# Testing

## Local

```
serverless invoke local --function create --path mocks/create-event.json
```

## Remote

See [this article](https://serverless-stack.com/chapters/test-the-apis.html) for details on testing the API which is secured by Cognito. Be sure that you have [created the test user in cognito](https://serverless-stack.com/chapters/create-a-cognito-test-user.html) first.
