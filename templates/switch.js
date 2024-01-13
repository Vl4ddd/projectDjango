function openTab(evt, tabName) {
    // Получаем все элементы с классом "tabcontent" и скрываем их
    var tabcontent = document.getElementsByClassName("tabcontent");
    for (var i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }

    // Получаем все элементы с классом "tablinks" и удаляем класс "active"
    var tablinks = document.getElementsByClassName("tablinks");
    for (var i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Отображаем текущую вкладку и добавляем класс "active" к кнопке
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
  }