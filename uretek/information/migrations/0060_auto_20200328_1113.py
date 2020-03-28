# Generated by Django 2.2.6 on 2020-03-28 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0059_auto_20200316_1759'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Контактная информация для контакты', 'verbose_name_plural': 'Контактная информация для контакты'},
        ),
        migrations.AlterModelOptions(
            name='contdecr',
            options={'verbose_name': 'Загловки на странице контакты', 'verbose_name_plural': 'Загловки на странице контакты'},
        ),
        migrations.AlterModelOptions(
            name='example',
            options={'verbose_name': 'Пример', 'verbose_name_plural': 'Примеры'},
        ),
        migrations.AlterModelOptions(
            name='faq',
            options={'verbose_name': 'Наполнение списка', 'verbose_name_plural': 'Наполнение списка'},
        ),
        migrations.AlterModelOptions(
            name='faqblock',
            options={'verbose_name': 'Всплвающие списки на старнице', 'verbose_name_plural': 'Всплвающие списки на старнице'},
        ),
        migrations.AlterModelOptions(
            name='footer',
            options={'verbose_name': 'Данные подвала', 'verbose_name_plural': 'Данные подвала'},
        ),
        migrations.AlterModelOptions(
            name='footercont',
            options={'verbose_name': 'Тип подвала', 'verbose_name_plural': 'Тип подвала'},
        ),
        migrations.AlterModelOptions(
            name='mpage',
            options={'verbose_name': 'Информации для главной', 'verbose_name_plural': 'Информации для главной'},
        ),
        migrations.AlterModelOptions(
            name='navconstruct',
            options={'verbose_name': 'Раздел', 'verbose_name_plural': 'Основное меню'},
        ),
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': 'Информация страницы', 'verbose_name_plural': 'Информация страницы'},
        ),
        migrations.AlterModelOptions(
            name='pagenext',
            options={'verbose_name': 'Иинформация страницы', 'verbose_name_plural': 'Иинформация страницы'},
        ),
        migrations.AlterModelOptions(
            name='pageproject',
            options={'verbose_name': 'Иинформация страницы', 'verbose_name_plural': 'Иинформация страницы'},
        ),
        migrations.AlterModelOptions(
            name='pictslider',
            options={'verbose_name': 'Слайдер на главной странице', 'verbose_name_plural': 'Слайдер на главной странице'},
        ),
        migrations.AlterModelOptions(
            name='pictures',
            options={'verbose_name': 'Фото примера', 'verbose_name_plural': 'Фото примера'},
        ),
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name': 'Типы примеров на странице', 'verbose_name_plural': 'Типы примеров на странице'},
        ),
        migrations.AlterModelOptions(
            name='short',
            options={'verbose_name': 'Краткая информация примера', 'verbose_name_plural': 'Краткая информация примера'},
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name': 'Картинки слайдера страницы', 'verbose_name_plural': 'Картинки слайдера страницы'},
        ),
        migrations.AlterModelOptions(
            name='social',
            options={'verbose_name': 'Социальная сеть', 'verbose_name_plural': 'Социальные сети и данные заголовка'},
        ),
        migrations.AlterModelOptions(
            name='subnavigator',
            options={'verbose_name': 'Подраздел', 'verbose_name_plural': 'Подменю'},
        ),
        migrations.AlterModelOptions(
            name='subsubnav',
            options={'verbose_name': 'Подраздел подраздела', 'verbose_name_plural': 'Подменю подменю'},
        ),
        migrations.AlterModelOptions(
            name='text',
            options={'verbose_name': 'Информация подвала', 'verbose_name_plural': 'Информация подвала'},
        ),
        migrations.AlterModelOptions(
            name='textslider',
            options={'verbose_name': 'Слайдер текст на главной странице', 'verbose_name_plural': 'Слайдер текст на главной странице'},
        ),
        migrations.AlterModelOptions(
            name='values',
            options={'verbose_name': 'Список информации для главной', 'verbose_name_plural': 'Список информации для главной'},
        ),
        migrations.RemoveField(
            model_name='pictures',
            name='href2',
        ),
        migrations.RemoveField(
            model_name='pictures',
            name='href3',
        ),
        migrations.AddField(
            model_name='navconstruct',
            name='alt',
            field=models.CharField(blank=True, help_text='описание картинки', max_length=150, verbose_name='Alt картинка'),
        ),
        migrations.AddField(
            model_name='subnavigator',
            name='alt',
            field=models.CharField(blank=True, help_text='описание картинки', max_length=150, verbose_name='Alt картинка'),
        ),
        migrations.AddField(
            model_name='subsubnav',
            name='alt',
            field=models.CharField(blank=True, help_text='описание картинки', max_length=150, verbose_name='Alt картинка'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='answer',
            field=models.TextField(blank=True, help_text='ответ списка', verbose_name='Ответ списка'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='icon',
            field=models.CharField(blank=True, help_text='стиль выбирается из https://fontawesome.ru/all-icons/ ', max_length=50, verbose_name='стиль иконки'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(help_text='имя списка', max_length=50, verbose_name='Имя списка'),
        ),
        migrations.AlterField(
            model_name='contdecr',
            name='title1',
            field=models.CharField(blank=True, help_text='Загловок на стр контакты', max_length=100, verbose_name='Загловок на стр контакты'),
        ),
        migrations.AlterField(
            model_name='contdecr',
            name='title2',
            field=models.CharField(blank=True, help_text='Загловок на стр контакты', max_length=100, verbose_name='Загловок на стр контакты'),
        ),
        migrations.AlterField(
            model_name='contdecr',
            name='title3',
            field=models.CharField(blank=True, help_text='Загловок на стр контакты', max_length=100, verbose_name='Загловок на стр контакты'),
        ),
        migrations.AlterField(
            model_name='example',
            name='description',
            field=models.TextField(blank=True, help_text='описание страницы в поискаовика', max_length=300, verbose_name='Описание страницы'),
        ),
        migrations.AlterField(
            model_name='example',
            name='example',
            field=models.ForeignKey(help_text='привязка к типу примера', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='example', to='information.Projects', verbose_name='Тип примеров'),
        ),
        migrations.AlterField(
            model_name='example',
            name='href',
            field=models.CharField(blank=True, help_text='URL картинки в приблежениии', max_length=200, verbose_name='URL картинки'),
        ),
        migrations.AlterField(
            model_name='example',
            name='keywords',
            field=models.TextField(blank=True, help_text='ключевые слова для поисковика', max_length=300, verbose_name='Ключевые слова'),
        ),
        migrations.AlterField(
            model_name='example',
            name='projectname',
            field=models.CharField(blank=True, help_text='название проекта', max_length=200, verbose_name='Название проекта'),
        ),
        migrations.AlterField(
            model_name='example',
            name='slug',
            field=models.SlugField(blank=True, help_text='название url адреса', null=True, unique=True, verbose_name='URL адрес'),
        ),
        migrations.AlterField(
            model_name='example',
            name='src',
            field=models.CharField(blank=True, help_text='URL картинки', max_length=200, verbose_name='URL картинки'),
        ),
        migrations.AlterField(
            model_name='example',
            name='title',
            field=models.CharField(blank=True, help_text='обозначается без ., пример type1', max_length=100, verbose_name='Тип примеров'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(blank=True, help_text='ответ списка', verbose_name='Ответ списка'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='name',
            field=models.ForeignKey(help_text='привязка к основному меню', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='faq', to='information.Faqblock', verbose_name='Основное меню'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.CharField(help_text='имя списка', max_length=200, verbose_name='Имя списка'),
        ),
        migrations.AlterField(
            model_name='faqblock',
            name='name',
            field=models.CharField(help_text='название списка и страница', max_length=100, verbose_name='Название списка'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='classdir',
            field=models.CharField(blank=True, help_text='Стиль контейнера', max_length=100, verbose_name='Стиль'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='classul',
            field=models.CharField(blank=True, help_text='указать стиль', max_length=100, verbose_name='Стиль'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='hreflogo',
            field=models.CharField(blank=True, help_text='URL лого', max_length=100, verbose_name='URL лого'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='title',
            field=models.CharField(help_text='название раздела подвала', max_length=30, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='type',
            field=models.ForeignKey(help_text='выбрать тип подвала', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type', to='information.Footercont', verbose_name='Тип подвала'),
        ),
        migrations.AlterField(
            model_name='footercont',
            name='classdiv',
            field=models.CharField(blank=True, help_text='Стиль контейнера', max_length=100, verbose_name='Стиль'),
        ),
        migrations.AlterField(
            model_name='footercont',
            name='classname',
            field=models.CharField(help_text='указать стиль', max_length=100, verbose_name='Стиль'),
        ),
        migrations.AlterField(
            model_name='footercont',
            name='title',
            field=models.CharField(help_text='название типа подвала', max_length=30, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='mpage',
            name='name',
            field=models.CharField(blank=True, help_text='заголовок', max_length=30, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='mpage',
            name='textblock',
            field=models.TextField(blank=True, help_text='текст', verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='mpage',
            name='textblock1',
            field=models.TextField(blank=True, help_text='текст', verbose_name='Текст1'),
        ),
        migrations.AlterField(
            model_name='mpage',
            name='title',
            field=models.CharField(blank=True, help_text='заголовок', max_length=100, verbose_name='Заголовок1'),
        ),
        migrations.AlterField(
            model_name='mpage',
            name='title1',
            field=models.CharField(blank=True, help_text='заголовок', max_length=100, verbose_name='Заголовок2'),
        ),
        migrations.AlterField(
            model_name='navconstruct',
            name='descrtionmeta',
            field=models.TextField(blank=True, help_text='описание страницы в поискаовика', max_length=300, verbose_name='Описание страницы'),
        ),
        migrations.AlterField(
            model_name='navconstruct',
            name='hreflogo',
            field=models.CharField(blank=True, help_text='URL картинка', max_length=100, verbose_name='URL картинка'),
        ),
        migrations.AlterField(
            model_name='navconstruct',
            name='keywordsmeta',
            field=models.TextField(blank=True, help_text='ключевые слова для поисковика', max_length=300, verbose_name='Ключевые слова'),
        ),
        migrations.AlterField(
            model_name='navconstruct',
            name='name',
            field=models.CharField(help_text='название основного раздела', max_length=30, verbose_name='Название раздела'),
        ),
        migrations.AlterField(
            model_name='navconstruct',
            name='section',
            field=models.TextField(help_text='название секции, необязательно', null=True, verbose_name='Название секции'),
        ),
        migrations.AlterField(
            model_name='navconstruct',
            name='slug',
            field=models.SlugField(blank=True, help_text='название url адреса', null=True, unique=True, verbose_name='URL адрес'),
        ),
        migrations.AlterField(
            model_name='navconstruct',
            name='template_name',
            field=models.CharField(help_text='название html файла', max_length=30, null=True, verbose_name='Название html'),
        ),
        migrations.AlterField(
            model_name='navconstruct',
            name='title',
            field=models.CharField(blank=True, help_text='описание заголовка в строке браузера', max_length=300, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='page',
            name='projname',
            field=models.ForeignKey(blank=True, help_text='привязка к подменю', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subtext', to='information.Subnavigator', verbose_name='Подменю'),
        ),
        migrations.AlterField(
            model_name='page',
            name='quote',
            field=models.TextField(blank=True, help_text='текст', verbose_name='Текст1'),
        ),
        migrations.AlterField(
            model_name='page',
            name='subname',
            field=models.ForeignKey(help_text='привязка к основному меню', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text', to='information.Navconstruct', verbose_name='Основное меню'),
        ),
        migrations.AlterField(
            model_name='page',
            name='textdown',
            field=models.TextField(blank=True, help_text='текст', verbose_name='Текст2'),
        ),
        migrations.AlterField(
            model_name='page',
            name='textup',
            field=models.TextField(blank=True, help_text='текст', verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(blank=True, help_text='название заголовка', max_length=30, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='pagenext',
            name='blockquote',
            field=models.TextField(blank=True, help_text='текст', verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='pagenext',
            name='paragraph',
            field=models.TextField(blank=True, help_text='текст', verbose_name='Текст1'),
        ),
        migrations.AlterField(
            model_name='pagenext',
            name='projname',
            field=models.ForeignKey(blank=True, help_text='привязка к подменю', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subnext', to='information.Subnavigator', verbose_name='Подменю'),
        ),
        migrations.AlterField(
            model_name='pagenext',
            name='quote',
            field=models.TextField(blank=True, help_text='текст', verbose_name='Текст4'),
        ),
        migrations.AlterField(
            model_name='pagenext',
            name='subname',
            field=models.ForeignKey(help_text='привязка к основному меню', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next', to='information.Navconstruct', verbose_name='Основное меню'),
        ),
        migrations.AlterField(
            model_name='pagenext',
            name='textdown',
            field=models.TextField(blank=True, help_text='текст', verbose_name='Текст5'),
        ),
        migrations.AlterField(
            model_name='pagenext',
            name='textnext',
            field=models.TextField(blank=True, help_text='текст', verbose_name='Текст2'),
        ),
        migrations.AlterField(
            model_name='pagenext',
            name='textup',
            field=models.TextField(blank=True, help_text='текст', verbose_name='Текст3'),
        ),
        migrations.AlterField(
            model_name='pagenext',
            name='title',
            field=models.CharField(blank=True, help_text='заголовок', max_length=100, verbose_name='Заголовок3'),
        ),
        migrations.AlterField(
            model_name='pagenext',
            name='titlecoloumn',
            field=models.CharField(blank=True, help_text='заголовок', max_length=100, verbose_name='Заголовок1'),
        ),
        migrations.AlterField(
            model_name='pagenext',
            name='titlenext',
            field=models.CharField(blank=True, help_text='заголовок', max_length=30, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='pagenext',
            name='titleparagraph',
            field=models.CharField(blank=True, help_text='заголовок', max_length=100, verbose_name='Заголовок2'),
        ),
        migrations.AlterField(
            model_name='pagenext',
            name='urljpg',
            field=models.CharField(blank=True, help_text='URL фото', max_length=100, verbose_name='URL фото'),
        ),
        migrations.AlterField(
            model_name='pagenext',
            name='urlvideo',
            field=models.URLField(blank=True, help_text='URL видео с ютуба', max_length=100, verbose_name='URL видео с ютуба'),
        ),
        migrations.AlterField(
            model_name='pageproject',
            name='blockquote',
            field=models.TextField(blank=True, help_text='текст', verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='pageproject',
            name='name',
            field=models.ForeignKey(help_text='привязка к примеру', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pageproject', to='information.Example', verbose_name='Пример'),
        ),
        migrations.AlterField(
            model_name='pageproject',
            name='paragraph',
            field=models.TextField(blank=True, help_text='текст', verbose_name='Текст1'),
        ),
        migrations.AlterField(
            model_name='pageproject',
            name='textnext',
            field=models.TextField(blank=True, help_text='текст', verbose_name='Текст2'),
        ),
        migrations.AlterField(
            model_name='pageproject',
            name='titlecoloumn',
            field=models.CharField(blank=True, help_text='заголовок', max_length=100, verbose_name='Заголовок1'),
        ),
        migrations.AlterField(
            model_name='pageproject',
            name='titlenext',
            field=models.CharField(blank=True, help_text='заголовок', max_length=30, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='pageproject',
            name='titleparagraph',
            field=models.CharField(blank=True, help_text='заголовок', max_length=100, verbose_name='Заголовок2'),
        ),
        migrations.AlterField(
            model_name='pageproject',
            name='urlvideo',
            field=models.URLField(blank=True, help_text='URL видео с ютуба', max_length=100, verbose_name='URL видео с ютуба'),
        ),
        migrations.AlterField(
            model_name='pictslider',
            name='hreflogo',
            field=models.CharField(help_text='URL фото', max_length=100, verbose_name='URL фото'),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='href1',
            field=models.CharField(blank=True, help_text='URL фото примера', max_length=200, verbose_name='URL фото'),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='name',
            field=models.ForeignKey(help_text='привязка к примеру', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='information.Example', verbose_name='Пример'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='dafilter',
            field=models.CharField(blank=True, help_text='обозначается через ., пример .type1', max_length=100, verbose_name='Обозначени типа'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='href',
            field=models.CharField(blank=True, help_text='ссылка на страницу, если на той же, по умолчанию #', max_length=100, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='projname',
            field=models.ForeignKey(blank=True, help_text='привязка к подменю', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subproj', to='information.Subnavigator', verbose_name='Подменю'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='subname',
            field=models.ForeignKey(help_text='привязка к основному меню', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proj', to='information.Navconstruct', verbose_name='Основное меню'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='title',
            field=models.CharField(blank=True, help_text='название тимпа примеров', max_length=100, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='short',
            name='caregory',
            field=models.CharField(help_text='Категория', max_length=100, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='short',
            name='duration',
            field=models.CharField(help_text='Сроки выполнения', max_length=100, verbose_name='Сроки выполнения'),
        ),
        migrations.AlterField(
            model_name='short',
            name='fokus',
            field=models.CharField(help_text='Фокус', max_length=100, verbose_name='Фокус'),
        ),
        migrations.AlterField(
            model_name='short',
            name='name',
            field=models.ForeignKey(help_text='привязка к примеру', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='short', to='information.Example', verbose_name='Пример'),
        ),
        migrations.AlterField(
            model_name='short',
            name='namecategory',
            field=models.CharField(help_text='Название категории', max_length=30, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='short',
            name='nameduration',
            field=models.CharField(help_text='Название сроков', max_length=30, verbose_name='Название сроков'),
        ),
        migrations.AlterField(
            model_name='short',
            name='namefokus',
            field=models.CharField(help_text='Название фокус', max_length=30, verbose_name='Название фокус'),
        ),
        migrations.AlterField(
            model_name='short',
            name='namesite',
            field=models.CharField(help_text='Название адреса', max_length=30, verbose_name='Название адреса'),
        ),
        migrations.AlterField(
            model_name='short',
            name='predescription',
            field=models.TextField(blank=True, help_text='Краткое описание', verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='short',
            name='site',
            field=models.CharField(help_text='Адрес проекта', max_length=100, verbose_name='Адрес проекта'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='hreflogo',
            field=models.CharField(blank=True, help_text='URL картинки', max_length=100, verbose_name='URL картинки'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='name',
            field=models.CharField(help_text='имя картинки на слайдере', max_length=30, verbose_name='Имя картинки'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='projname',
            field=models.ForeignKey(blank=True, help_text='привязка к подменю', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subslider', to='information.Subnavigator', verbose_name='Подменю'),
        ),
        migrations.AlterField(
            model_name='social',
            name='classname',
            field=models.CharField(help_text='стиль выбирается из https://fontawesome.ru/all-icons/ ', max_length=30, verbose_name='стиль иконки'),
        ),
        migrations.AlterField(
            model_name='social',
            name='href',
            field=models.URLField(help_text='URL сети или сайта', null=True, verbose_name='URL компании'),
        ),
        migrations.AlterField(
            model_name='social',
            name='social',
            field=models.BooleanField(help_text='Если соц сеть,то ставим галочку', verbose_name='Соц сети'),
        ),
        migrations.AlterField(
            model_name='social',
            name='text',
            field=models.TextField(blank=True, help_text='Описание компании или сети', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='social',
            name='title',
            field=models.CharField(help_text='название подменю', max_length=30, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='subnavigator',
            name='descrtionmeta',
            field=models.TextField(blank=True, help_text='описание страницы в поискаовика', max_length=300, verbose_name='Описание страницы'),
        ),
        migrations.AlterField(
            model_name='subnavigator',
            name='hreflogo',
            field=models.CharField(blank=True, help_text='URL картинка', max_length=100, verbose_name='URL картинка'),
        ),
        migrations.AlterField(
            model_name='subnavigator',
            name='keywordsmeta',
            field=models.TextField(blank=True, help_text='ключевые слова для поисковика', max_length=300, verbose_name='Ключевые слова'),
        ),
        migrations.AlterField(
            model_name='subnavigator',
            name='name',
            field=models.CharField(help_text='название основного раздела', max_length=30, verbose_name='Название раздела'),
        ),
        migrations.AlterField(
            model_name='subnavigator',
            name='projname',
            field=models.ForeignKey(blank=True, help_text='привязка к подвалу', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='information.Footercont', verbose_name='Тип подвала'),
        ),
        migrations.AlterField(
            model_name='subnavigator',
            name='section',
            field=models.TextField(help_text='название секции, необязательно', null=True, verbose_name='Название секции'),
        ),
        migrations.AlterField(
            model_name='subnavigator',
            name='slug',
            field=models.SlugField(blank=True, help_text='название url адреса', null=True, unique=True, verbose_name='URL адрес'),
        ),
        migrations.AlterField(
            model_name='subnavigator',
            name='subname',
            field=models.ForeignKey(blank=True, help_text='привязка к основному меню', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub', to='information.Navconstruct', verbose_name='Основное меню'),
        ),
        migrations.AlterField(
            model_name='subnavigator',
            name='template_name',
            field=models.CharField(help_text='название html файла', max_length=30, null=True, verbose_name='Название html'),
        ),
        migrations.AlterField(
            model_name='subnavigator',
            name='title',
            field=models.CharField(blank=True, help_text='описание заголовка в строке браузера', max_length=300, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='subsubnav',
            name='descrtionmeta',
            field=models.TextField(blank=True, help_text='описание страницы в поискаовика', max_length=300, verbose_name='Описание страницы'),
        ),
        migrations.AlterField(
            model_name='subsubnav',
            name='hreflogo',
            field=models.CharField(blank=True, help_text='URL картинка', max_length=100, verbose_name='URL картинка'),
        ),
        migrations.AlterField(
            model_name='subsubnav',
            name='keywordsmeta',
            field=models.TextField(blank=True, help_text='ключевые слова для поисковика', max_length=300, verbose_name='Ключевые слова'),
        ),
        migrations.AlterField(
            model_name='subsubnav',
            name='name',
            field=models.CharField(help_text='название основного раздела', max_length=30, verbose_name='Название раздела'),
        ),
        migrations.AlterField(
            model_name='subsubnav',
            name='section',
            field=models.TextField(help_text='название секции, необязательно', null=True, verbose_name='Название секции'),
        ),
        migrations.AlterField(
            model_name='subsubnav',
            name='slug',
            field=models.SlugField(blank=True, help_text='название url адреса', null=True, unique=True, verbose_name='URL адрес'),
        ),
        migrations.AlterField(
            model_name='subsubnav',
            name='subname',
            field=models.ForeignKey(help_text='привязка к подменю', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub', to='information.Subnavigator', verbose_name='Подменю'),
        ),
        migrations.AlterField(
            model_name='subsubnav',
            name='template_name',
            field=models.CharField(help_text='название html файла', max_length=30, null=True, verbose_name='Название html'),
        ),
        migrations.AlterField(
            model_name='subsubnav',
            name='title',
            field=models.CharField(blank=True, help_text='описание заголовка в строке браузера', max_length=300, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='text',
            name='footertext',
            field=models.TextField(blank=True, help_text='описание подвала', verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='text',
            name='subname',
            field=models.ForeignKey(help_text='привязка к данным подвала', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='textsub', to='information.Footer', verbose_name='Данные подвала'),
        ),
        migrations.AlterField(
            model_name='text',
            name='title',
            field=models.CharField(blank=True, help_text='название раздела подвала', max_length=30, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='textslider',
            name='clas',
            field=models.CharField(blank=True, help_text='текст', max_length=20, verbose_name='Класс текста слайдера'),
        ),
        migrations.AlterField(
            model_name='textslider',
            name='picture',
            field=models.ForeignKey(help_text='привязка к слайдеру главной страницы', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='picture', to='information.Pictslider', verbose_name='Слайдер главной страницы'),
        ),
        migrations.AlterField(
            model_name='textslider',
            name='textbldown',
            field=models.TextField(blank=True, help_text='текст', verbose_name='Текст слайедра'),
        ),
        migrations.AlterField(
            model_name='textslider',
            name='textblock',
            field=models.TextField(blank=True, help_text='текст', verbose_name='Текст слайедра'),
        ),
        migrations.AlterField(
            model_name='values',
            name='answer',
            field=models.TextField(blank=True, help_text='ответ списка', verbose_name='Ответ списка'),
        ),
        migrations.AlterField(
            model_name='values',
            name='icon',
            field=models.CharField(blank=True, help_text='стиль выбирается из https://fontawesome.ru/all-icons/ ', max_length=50, verbose_name='стиль иконки'),
        ),
        migrations.AlterField(
            model_name='values',
            name='name',
            field=models.CharField(help_text='имя списка', max_length=50, verbose_name='Имя списка'),
        ),
    ]