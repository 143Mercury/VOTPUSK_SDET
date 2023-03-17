import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver


class BaseMethods(BasePage):
    # методы для взаимодействия с элементами страницы
    def __init__(self, driver):
        super().__init__(driver)

    def click_element(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(by_locator)
            )
            element.click()
        except Exception as e:
            print("Test should to be able to pass")
            print(e)

    def send_keys_to_element(self, by_locator, keys):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(by_locator)
            )
            element.clear()
            element.send_keys(keys)
        except Exception as e:
            print("Can't find an element")
            print(e)

    def wait_until_element_clickable(self, by_locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(by_locator))

    def wait_until_element_visible(self, by_locator, timeout=10, poll_frequency=0.5):
        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        wait.until(EC.visibility_of_element_located(by_locator))

    def double_click_element(self, by_locator, double_click=True):
        element = self.driver.find_element(*by_locator)
        if double_click:
            action = ActionChains(self.driver)
            action.double_click(element).perform()
        else:
            element.click()

    def click_element_nw(self, by_locator):
        element = self.driver.find_element(by_locator)
        element.click()

    def assert_element_visibility(self, by_locator, timeout=15):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(by_locator)
            )
            assert element.is_displayed()
            assert element.location_once_scrolled_into_view == element.location
            print(f"Тест пройден успешно: элемент {by_locator} виден на странице")
        except Exception as e:
            print(f"Тест пройден не успешно: элемент {by_locator} или элемент вне зоны видимости ")
            print(f"Причина: {str(e)}")

    def assert_element_to_be_clickable(self, by_locator, timeout=15):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(by_locator)
            )
            assert element.is_displayed()
            assert element.location_once_scrolled_into_view == element.location
            print(f"Тест пройден успешно: элемент{by_locator} виден на странице")
        except Exception as e:
            print(f"Причина: {str(e)}")

    def assert_text_visibility(self, text):
        try:
            element_present = EC.presence_of_element_located(
                (By.XPATH, f"//*[contains(text(), '{text}')]")
            )
            element_visible = EC.visibility_of_element_located(
                (By.XPATH, f"//*[contains(text(), '{text}')]")
            )
            WebDriverWait(self.driver, 10).until(element_present)
            assert WebDriverWait(self.driver, 10).until(element_visible).is_displayed()
            print(f"Text '{text}' is visible on the page")
        except Exception as e:
            print(f"Error: {e}")
            raise AssertionError(f"Text '{text}' is not visible on the page")

    def wait_until_element_loaded(self, by_locator, timeout=20):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(by_locator)
            )
            assert element.is_displayed(), f"Элемент {by_locator} не виден на странице"
        except TimeoutException:
            assert False, f"Элемент {by_locator} не найден на странице после {timeout} секунд ожидания"

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)
        )
        return bool(element)

    def scroll_page(self, scroll_by=300):
        script = f"window.scrollBy(0, {scroll_by})"
        self.driver.execute_script(script)

    def assert_elements_exist(self, by_locator):
        elements = self.driver.find_elements(*by_locator)
        assert len(elements) > 0, f"No elements found with locator {by_locator}."

    def click_random_locator(self, locators):
        random_locator = random.choice(locators)
        self.driver.find_element(*random_locator).click()

    def click_random_enabled_day_in_calendar(self, calendar_locator):
        # кликнуть на локатор виджета календаря
        self.driver.find_element(*calendar_locator).click()
        # найти все элементы в календаре, имеющие тег "td"
        day_elements = self.driver.find_elements(By.CSS_SELECTOR, ".ui-datepicker-calendar td")
        # создать список кликабельных чисел
        enabled_days = []
        for day in day_elements:
            if "ui-state-disabled" not in day.get_attribute("class"):
                enabled_days.append(day)

        # если нет кликабельных чисел, выбросить исключение
        if not enabled_days:
            raise NoSuchElementException("No enabled days found in the calendar widget.")

        # выбрать случайное число из списка кликабельных чисел
        random_day = None
        while not random_day:
            random_day = random.choice(enabled_days)
            if "ui-state-disabled" in random_day.get_attribute("class"):
                random_day = None
                time.sleep(1)

        # кликнуть на выбранное число
        random_day.click()

    def select_random_option_from_dropdown(self, dropdown_element):
        """Selects a random option from a given dropdown menu element"""
        # Click on the dropdown menu to open it
        dropdown_element.click()

        # Get all available options in the dropdown
        options = dropdown_element.find_elements_by_tag_name("option")

        # Select a random option from the dropdown (excluding the first one)
        random_option = random.choice(options[1:])

        # Click on the random option to select it
        random_option.click()

        # Click on the page body to close the dropdown menu
        body = self.driver.find_element_by_tag_name("body")
        body.send_keys(Keys.ESCAPE)

    def random_country_selection(self, dropdown_country):
        driver = self.driver
        action = ActionChains(driver)
        enter_pressed = False
        while True:
            action.send_keys(Keys.DOWN).perform()
            time.sleep(0.5)
            dropdown = driver.find_element(*dropdown_country)  # Ищем элемент по локатору
            if not dropdown.is_displayed():
                break
            if random.randint(1, 10) == 3:
                time.sleep(random.uniform(0.5, 2.0))
                action.send_keys(Keys.ENTER).perform()
                enter_pressed = True
                break

    def do_randint_click(self, by_locator, count=5, scroll=False):
        for i in range(count):
            try:
                elements = WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(by_locator))
                element = random.choice(elements)
                if scroll:
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                element.click()
                WebDriverWait(self.driver, 5).until(EC.staleness_of(element))
            except (StaleElementReferenceException, TimeoutException):
                pass

    def scroll_page_second(self, scroll_by=125):
        script = f"window.scrollBy(0, {scroll_by})"
        self.driver.execute_script(script)

    def select_random_widget_item_by_xpath(self, widget, xpath):
        # Находим список элементов виджета
        items = widget.find_elements_by_xpath(xpath)

        # Выбираем случайный элемент из списка
        random_item = random.choice(items)

        # Создаем экземпляр ActionChains
        action = ActionChains(self.driver)

        # Кликаем на случайный элемент
        action.move_to_element(random_item).click().perform()

    def wait_for_element(self, locator, timeout=10):
        """ Явное ожидание элемента на странице """
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            raise Exception(f"Элемент не найден на странице за {timeout} секунд")

    def check_container_block(self, container_locator, block_locator, timeout=10):
        try:
            # Ожидаем появления контейнера
            container = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(container_locator)
            )
            # Получаем список всех блоков в контейнере
            blocks = container.find_elements(*block_locator)
            # Проверяем, что список блоков не пустой
            assert len(blocks) > 0, "Блоки не найдены в контейнере"
        except TimeoutException:
            raise TimeoutException(f"Контейнер не был найден за {timeout} секунд")
        except NoSuchElementException:
            raise NoSuchElementException("Блок не найден")

    def check_container(self, container_locator, timeout=10):
        try:
            # Ожидаем появления контейнера
            container = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(container_locator)
            )
        except TimeoutException:
            raise TimeoutException(f"Контейнер не был найден за {timeout} секунд")
        except NoSuchElementException:
            raise NoSuchElementException("Контейнер не найден")

    def scroll_page_tours(self, scroll_by=650):
        script = f"window.scrollBy(0, {scroll_by})"
        self.driver.execute_script(script)

    def scroll_page_articles(self, scroll_by=1175):
        script = f"window.scrollBy(0, {scroll_by})"
        self.driver.execute_script(script)

    def scroll_page_attractions(self, scroll_by=1750):
        script = f"window.scrollBy(0, {scroll_by})"
        self.driver.execute_script(script)

    def scroll_page_hotels(self, scroll_by=2150):
        script = f"window.scrollBy(0, {scroll_by})"
        self.driver.execute_script(script)

    def scroll_page_train(self, scroll_by=2550):
        script = f"window.scrollBy(0, {scroll_by})"
        self.driver.execute_script(script)

    def scroll_page_туцы(self, scroll_by=3525):
        script = f"window.scrollBy(0, {scroll_by})"
        self.driver.execute_script(script)

    def scroll_page_scopes(self, scroll_by=3525):
        script = f"window.scrollBy(0, {scroll_by})"
        self.driver.execute_script(script)

    def scroll_page_other_delay(self, scroll_by=3975):
        script = f"window.scrollBy(0, {scroll_by})"
        self.driver.execute_script(script)

    def scroll_page_comment(self, scroll_by=4475):
        script = f"window.scrollBy(0, {scroll_by})"
        self.driver.execute_script(script)

    def check_container_blocks_with_arrows(self, container_locator, next_arrow_locator, prev_arrow_locator, timeout=10):
        try:
            # Ожидаем появления контейнера
            container = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(container_locator)
            )

            # Получаем количество блоков в контейнере
            num_blocks = len(container.find_elements(By.CSS_SELECTOR, '*'))

            # Кликаем на стрелки для прокрутки контейнера
            while True:
                try:
                    next_arrow = container.find_element(*next_arrow_locator)
                    next_arrow.click()
                except NoSuchElementException:
                    break

            while True:
                try:
                    prev_arrow = container.find_element(*prev_arrow_locator)
                    prev_arrow.click()
                except NoSuchElementException:
                    break

            # Проверяем, что список блоков не пустой
            try:
                container = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located(container_locator)
                )
                blocks = container.find_elements(By.CSS_SELECTOR, '*')
                assert len(blocks) == num_blocks, "Неверное количество блоков в контейнере"
            except TimeoutException:
                raise TimeoutException(f"Контейнер не был найден за {timeout} секунд")
            except NoSuchElementException:
                raise NoSuchElementException("Блок не найден")

        except TimeoutException:
            raise TimeoutException(f"Контейнер не был найден за {timeout} секунд")
        except NoSuchElementException:
            raise NoSuchElementException("Элемент не найден")

    def click_through_container_blocks(self, container_selector, next_selector, prev_selector, timeout=10):
        """
        Метод осуществляет клик по стрелкам навигации контейнера для прокрутки блоков
        и проверяет наличие блоков в контейнере

        :param container_selector: селектор контейнера
        :param next_selector: селектор кнопки "следующий"
        :param prev_selector: селектор кнопки "предыдущий"
        :param timeout: время ожидания элемента в секундах
        """
        try:
            # Ожидаем появления контейнера
            container = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(container_selector)
            )
            # Получаем список всех блоков в контейнере
            blocks = container.find_elements_by_xpath("./*")
            # Проверяем, что список блоков не пустой
            assert len(blocks) > 0, "Блоки не найдены в контейнере"

            # Кликаем на кнопку "следующий" до тех пор, пока она не станет неактивной
            next_button = self.driver.find_element_by_css_selector(next_selector)
            while next_button.is_enabled():
                next_button.click()
                # Ожидаем, пока не загрузится следующий блок
                WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((By.XPATH, f"{container_selector}/*[position()={len(blocks) + 1}]"))
                )
                blocks = container.find_elements_by_xpath("./*")

            # Кликаем на кнопку "предыдущий" до тех пор, пока она не станет неактивной
            prev_button = self.driver.find_element_by_css_selector(prev_selector)
            while prev_button.is_enabled():
                prev_button.click()
                # Ожидаем, пока не загрузится предыдущий блок
                WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((By.XPATH, f"{container_selector}/*[position()={len(blocks)}]"))
                )
                blocks = container.find_elements_by_xpath("./*")

        except TimeoutException:
            raise TimeoutException(f"Контейнер не был найден за {timeout} секунд")
        except NoSuchElementException:
            raise NoSuchElementException("Блок не найден")

    def do_infinite_click(self, by_locator, scroll=False):
        """
        Метод осуществляет бесконечный клик по заданному локатору, пока элемент доступен для клика.
        :param by_locator: локатор элемента, на который необходимо кликнуть
        :param scroll: флаг прокрутки элемента в область видимости перед кликом (True/False)
        """
        while True:
            try:
                elements = WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(by_locator))
                for element in elements:
                    try:
                        if scroll:
                            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                        element.click()
                        # Ожидаем прогрузки элементов после клика
                        WebDriverWait(self.driver, 5).until(EC.staleness_of(element))
                    except StaleElementReferenceException:
                        pass
            except TimeoutException:
                break

    def is_element_present(self, by_locator):
        try:
            element = self.driver.find_element(*by_locator)
            return element.is_displayed()
        except NoSuchElementException:
            return False
