EN:
small site for department
working tab - "ЦАС НСИ"

realize:
- user's authorization, after this user can see hidden shape with important information (login / passwd: vadim / 123);
- logout from the account;
- able to stay on this same page, after authorization;
- add information to the database using form on this page;
- display information from the database on the page;
- able to add files to the server;
- find same information in the database and display it on the page;
- keeping of a log file;
- adding and linking additional fields in the administrator table;
- delete function for records from the database on the page;
- edit function for records from the database on the page;
- work in practice at internationalization localization (using blocktrans tag and ugettext_lazy, ugettext functions);
- createing site (using html, css).





RU:
небольшой сайт под нужды отдела

реализовано:
- авторизация пользователей, после авторизации видны скрытые от анонимных пользователей таблицы с важной информацией (login/passwd:  vadim/123);
- выход из аккаунта;
- возможноcть оставаться на этой же странице, после авторизации;
- добавление информации в БД с формы на странице;
- отображение информации из БД на странице;
- возможность добавлять файлы на сервер;
- поиск нужной информации в БД и вывод ее на страницу;
- ведения лог-файла;
- добавления дополнительного поля в таблицу администратора (т.е. данные об администраторах тянет из таблицы БД администраторов django проекта, в которой нет поля для ввода отчества, добавлено это поле и привязано к соответствующему пользователю);
- реализована функция удаления записи из БД на форме;
- реализована функция редактирования записи в БД;
- реализована интернационализация и локализация при помощи тега blocktrans и функций ugettext_lazy и ugettext);
- верстка сайта (html, css).


кратко по навигации:
рабочая вкладка - "ЦАС НСИ"




Django==1.7
Python==3.2.3

