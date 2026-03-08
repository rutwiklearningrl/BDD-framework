# features/environment.py
import allure

def after_step(context, step):
    if step.status == "failed":
        if hasattr(context, "driver"):
            allure.attach(
                context.driver.get_screenshot_as_png(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
