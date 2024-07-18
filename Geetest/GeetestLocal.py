import bili_ticket_gt_python

click = bili_ticket_gt_python.ClickPy()


def passGeetest(geetest, challenge):
    global click
    validate = click.simple_match_retry(geetest, challenge)
    data = {
        "success": True,
        "challenge": challenge,
        "validate": validate,
        "seccode": validate,
    }
    return data
