import time
from agent.intent_parser import parse_command
from agent.strategy_engine import should_execute
from listener.price_listener import get_price
from bot.execution_bot import execute_trade
from notifications.telegram_bot import send_message

command = parse_command("monitor MNT drop 10%")

last_price = get_price()

while True:

    current_price = get_price()

    if should_execute(last_price, current_price, command["drop_threshold"]):

        tx = execute_trade(
            command["token_in"],
            command["token_out"],
            1000
        )

        send_message(f"Swap executed: {tx}")

    last_price = current_price

    time.sleep(5)
