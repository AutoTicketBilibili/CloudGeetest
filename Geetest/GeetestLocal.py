import BasicInfo


def passGeetest(geetest, challenge):
    validate = BasicInfo.click.simple_match_retry(geetest, challenge)
    data = {
        "success": True,
        "challenge": challenge,
        "validate": validate,
        "seccode": validate,
    }
    return data
