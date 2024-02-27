import unittest
from unittest.mock import MagicMock

class TestLambdaHandler(unittest.TestCase):
    def test_lambda_handler(self):
        # Mocking the table object
        table = MagicMock()
        table.get_item.return_value = {'Item': {'value': 5}}
        table.update_item.return_value = None

        # Mocking the event and context objects
        event = {}
        context = {}

        # Calling the lambda_handler function
        result = lambda_handler(event, context)

        # Asserting the expected value
        self.assertEqual(result, 6)
        table.get_item.assert_called_once_with(Key={'id': 'count'})
        table.update_item.assert_called_once_with(
            Key={'id': 'count'},
            UpdateExpression='SET #v = :val',
            ExpressionAttributeNames={'#v': 'value'},
            ExpressionAttributeValues={':val': 6}
        )

if __name__ == '__main__':
    unittest.main()