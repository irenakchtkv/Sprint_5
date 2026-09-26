from selenium.webdriver.common.by import By

LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, './/button[text()="Войти в аккаунт"]')  # кнопка Войти в аккаунт на главной странице
REGISTER_LINK = (By.XPATH, './/a[text()="Зарегистрироваться"]')  # ссылка Зарегистрироваться под формой для авторизации
NAME_INPUT_REG = (By.XPATH, './/label[text()="Имя"]/parent::div/input')  # поле ввода Имя в форме регистрации
EMAIL_INPUT_REG = (By.XPATH, './/label[text()="Email"]/parent::div/input')  # поле ввода Email в форме регистрации
PASSWORD_INPUT_REG = (By.XPATH, './/label[text()="Пароль"]/parent::div/input')  # поле ввода Пароль в форме регистрации
REGISTER_BUTTON = (By.XPATH, './/button[text()="Зарегистрироваться"]')  # кнопка Зарегистрироваться под формой для регистрации
LOGIN_TITLE = (By.XPATH, './/h2[text()="Вход"]')  # заголовок Вход над формой авторизации
ERROR_MESSAGE = (By.XPATH, './/p[text()="Некорректный пароль"]')  # сообщение Некорректный пароль в форме регистрации

PERSONAL_ACCOUNT_BUTTON = (By.XPATH, './/p[text()="Личный Кабинет"]')  # кнопка Личный кабинет на главной странице
EMAIL_INPUT_AUTH = (By.XPATH, './/label[text()="Email"]/parent::div/input')  # поле ввода Email в форме авторизации
PASSWORD_INPUT_AUTH = (By.XPATH, './/label[text()="Пароль"]/parent::div/input')  # поле ввода Пароль в форме авторизации
LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]')  # кнопка Войти в форме авторизации
LOGIN_LINK_REG = (By.XPATH, './/a[text()="Войти"]')  # ссылка Войти под формой регистрации
RECOVER_PASSWORD_LINK = (By.XPATH, './/a[text()="Восстановить пароль"]')  # ссылка Восстановить пароль под формой авторизации
LOGIN_LINK_RECOVERY = (By.XPATH, './/a[text()="Войти"]')  # ссылка Войти под формой для восстановления пароля
PLACE_AN_ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')  # кнопка Оформить заказ на главной странице

PROFILE_SECTION = (By.XPATH, './/a[text()="Профиль"]')  # раздел Профиль в личном кабинете

CONSTRUCTOR_BUTTON = (By.XPATH, './/p[text()="Конструктор"]')  # ссылка Конструктор
BURGER_ASSEMBLE_TITLE = (By.XPATH, './/h1[text()="Соберите бургер"]')  # заголовок Соберите бургер
STELLAR_BURGERS_LOGO = (By.XPATH, './/div[@class="AppHeader_header__logo__2D0X2"]/a')  # логотип

LOGOUT_BUTTON = (By.XPATH, './/button[text()="Выход"]')  # кнопка Выход в личном кабинете

BUNS_BUTTON = (By.XPATH, './/span[text()="Булки"]')  # кнопка Булки
BUNS_SECTION = (By.XPATH, './/span[text()="Булки"]/parent::div')  # раздел Булки
SAUCES_BUTTON = (By.XPATH, './/span[text()="Соусы"]')  # кнопка Соусы
SAUCES_SECTION = (By.XPATH, './/span[text()="Соусы"]/parent::div')  # раздел Соусы
FILLINGS_BUTTON = (By.XPATH, './/span[text()="Начинки"]')  # кнопка Начинки
FILLINGS_SECTION = (By.XPATH, './/span[text()="Начинки"]/parent::div')  # раздел Начинки
