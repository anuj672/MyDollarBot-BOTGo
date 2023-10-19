import unittest
from unittest.mock import patch, Mock
from code.budget_max import run, post_max_budget

# Sample data for testing
EXAMPLE_USER_DATA = {
    '123': {
        'budget': {
            'max_per_txn_spend': 50
        }
    }
}

@patch('code.budget_max.helper.isMaxTransactionLimitAvailable', return_value=True)
@patch('code.budget_max.helper.getMaxTransactionLimit', return_value=100)  # Replace with actual values
@patch('telebot.telebot')
def test_run_with_existing_limit(mock_bot, mock_max_limit, mock_limit_available):
    # Simulate a message that triggers the run function
    message = Mock()

    # Call the run function
    run(message, mock_bot)

    # Check if the bot sends the correct message to update the max limit
    mock_bot.send_message.assert_called_with(message.chat.id, 'Current Limit is $100\n\nHow much is your new Max limit per transaction? \n(Enter numeric values only)')

@patch('telebot.telebot')
@patch('code.budget_max.helper.validate_entered_amount', return_value=50)  # Replace with a valid amount
@patch('code.budget_max.helper.read_json', return_value=EXAMPLE_USER_DATA)  # Replace with your data
@patch('code.budget_max.helper.write_json', return_value=True)  # Replace with success value
def test_post_max_budget_with_valid_amount(mock_bot, mock_validate_amount, mock_read_json, mock_write_json):
    # Simulate a message with a valid amount
    message = Mock()
    message.text = '50'

    # Call the post_max_budget function
    user_list = post_max_budget(message, mock_bot)

    # Check if the bot sends the 'Max Limit Updated!' message
    mock_bot.send_message.assert_called_with(message.chat.id, 'Max Limit Updated!')

    # Check if the user list was updated correctly
    assert user_list['123']['budget']['max_per_txn_spend'] == 50

if __name__ == '__main__':
    unittest.main()
