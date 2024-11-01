
class Locators:
     captcha_div = '//div[@id="modal-captcha" and @aria-hidden="false"]'
     captcha_submit_button = '//button[text()="Submit"]'
     captcha_error_paragraph = '//p[@id="captcha-error-message" and not(contains(@class,"hidden"))]'

     
     first_name_input_box = '//input[@id="offender-first-name"]'
     last_name_input_box = '//input[@id="offender-last-name"]'
     search_button = '//button[text()="Search"]'
     no_results = '//div[@id="modal-generic-error" and @aria-hidden="false"]'
     ok_button = '//button[text()="Ok"]'
     
     offender_tab = '//a[text()="Offender Search"]/parent::li[@class="active"]'
     offender_name = '//div[contains(@id,"name")]'
     first_names = '//span[@data-bind="text: FirstName"]'
     last_names = '//span[@data-bind="text: LastName"]'

     first_name = '//h3/span[@data-bind="text: FirstName"]'
     last_name = '//h3/span[@data-bind="text: LastName"]'
     label = '//fieldset[1]/label'
     value = './following-sibling::span'
     #values = '//fieldset[1]/label/following-sibling::span'

     disabled_next_button = '//button[contains(@data-bind, "click: nextPage") and contains(@class, "disabled") and following-sibling::div[not(contains(text(), "Page 0 of 0 (0 offenders found)"))]]'
     next_button = '//button[contains(@data-bind, "click: nextPage") and following-sibling::div[not(contains(text(), "Page 0 of 0 (0 offenders found)"))]]'

