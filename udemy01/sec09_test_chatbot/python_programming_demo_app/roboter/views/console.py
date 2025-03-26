from string import Template


def get_user_input(prompt):
    """ユーザーの入力を受け取る"""
    return input(prompt)


def get_template(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return Template(content)
