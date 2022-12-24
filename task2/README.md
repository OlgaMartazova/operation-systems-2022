# Task 2
## Файловые системы
1. `fdisk -l`  Просмотр таблицы жестких дисков.

![image](https://user-images.githubusercontent.com/71041400/209442788-b6960f9b-d6a6-4046-9a5a-dec02fedc464.png)

Добавленному диску соответствует `/dev/sdb`.

2. Размечаем добавленный диск на два раздела с помощью команды `fdisk /dev/sdb`. 
- Размечаем в формате GPT, создаем пустую таблицу ключом `g`;
- Создаем новую партицию ключом `n`;
- `1` - номер раздела, `2048` - начальный сектор раздела, `8390656` - размер раздела, что равняется 4G.
- Аналогично второй раздел, на кжадом шаге нажимая `enter` для выбора по умолчанию. Размер второго раздела, соответственно, 6G.
- Сохраняем ключом `w`.

Вызывая команду `lsblk`, проверяем созданные разделы:

![image](https://user-images.githubusercontent.com/71041400/209443227-21cebd44-436a-4f5d-9ecf-5599284f81b7.png)

4. Добавляем разделы в соответствующие файловые системы

![image](https://user-images.githubusercontent.com/71041400/209443276-4506ff8f-9328-44eb-8b2f-3d8b56f0b82e.png)

`tune2fs -m 5 /dev/sdb1` и `tune2fs -m 0 /dev/sdb2` - резервируем 5% и 0% для первого и второго раздела.

5. `mkdir` - создаем директории  `/media/docs` и `/mnt/work`.

6. Монтируем эти директории в разделы. Добавляем и сохраняем о них в `/etc/fstab`, чтобы информация о директориях сохранялась для следующего запуска виртуальной машины.

![image](https://user-images.githubusercontent.com/71041400/209443614-aa1fa706-6c2b-465e-a896-d6d4dd75a993.png)

````
/dev/sdb1       /media/docs     ext4    defaults        0       0
/dev/sdb2       /mnt/work       ext2    defaults        0       0
````

## Пользователи
7. Создаем нужные группы и пользователей

![image](https://user-images.githubusercontent.com/71041400/209443769-1a3ae0f2-0814-4bf8-b83e-1cf5e3677e53.png)

Командой `more /etc/group` проверяем перечень имеющихся в системе групп.

![image](https://user-images.githubusercontent.com/71041400/209443837-c017b862-04f7-4aeb-b71f-710f87a79645.png)

## Директории
8. Создаем поддиректории и назначаем владельца, группу владельца и права доступа.

![image](https://user-images.githubusercontent.com/71041400/209443906-f45d13d9-966b-4634-a353-a7376a3a4bf1.png)

`woody:developers` указывает на владельца и группу владельца. Права доступа назначаются для u (users), g(groups), o(others).

9. Добавляем следящие символьные ссылки

````
ln -s /media/docs/manuals /mnt/work/developers/docs
ln -s /media/docs/todo /mnt/work/developers/todo
````

![image](https://user-images.githubusercontent.com/71041400/209444270-a30ab4ce-df71-47c3-affe-c949bb94ab34.png)
