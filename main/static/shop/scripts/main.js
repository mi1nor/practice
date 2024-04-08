// menu__list--open
const menuBtn = document.querySelector(".menu__btn");
const menuClose = document.querySelector(".menu__close");
const menuList = document.querySelector(".menu__list");

menuBtn.addEventListener("click",()=>{
    menuList.classList.toggle("menu__list--open");
    menuBack.classList.toggle("menu--open");
});
menuClose.addEventListener("click",()=>{
    menuList.classList.remove("menu__list--open");
    menuBack.classList.remove("menu--open");
});

// Анимаций для добавления в корзину

function handleAddToCart(event) {
    event.preventDefault(); // Предотвращаем переход по ссылке
  
    // Получаем URL для запроса из атрибута href ссылки
    const url = event.target.href;
  
    // Отправляем GET запрос на сервер для добавления товара в корзину
    // Примечание: здесь используется GET запрос для простоты примера,
    // в реальном приложении лучше использовать POST запрос
    fetch(url)
      .then(response => {
        if (response.ok) {
          // Если запрос выполнен успешно, показываем уведомление
          addCartMessage();
        } else {
          // Если возникла ошибка при добавлении товара в корзину, выводим сообщение в консоль
          console.error('Ошибка при добавлении товара в корзину');
        }
      })
      .catch(error => {
        // Если возникла ошибка при выполнении запроса, выводим сообщение в консоль
        console.error('Ошибка при добавлении товара в корзину:', error);
      });
  }
  
  // Функция для показа уведомления о добавлении товара в корзину
  function addCartMessage() {
    Swal.fire({
      title: 'Товар добавлен в корзину',
      icon: 'success',
      showConfirmButton: false,
      timer: 1500 // Задержка перед закрытием уведомления (в миллисекундах)
    });
  }