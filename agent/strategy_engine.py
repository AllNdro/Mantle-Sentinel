def should_execute(prev_price, current_price, threshold):

    drop = (prev_price - current_price) / prev_price

    return drop >= threshold
