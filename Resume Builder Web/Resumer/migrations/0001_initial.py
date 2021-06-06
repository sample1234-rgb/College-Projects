# Generated by Django 3.1.7 on 2021-03-16 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievement', models.TextField(verbose_name='Achievement')),
            ],
        ),
        migrations.CreateModel(
            name='Addresse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address1', models.TextField()),
                ('Address2', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cont1', models.IntegerField(max_length=12, verbose_name='Contact 1')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=20, verbose_name='Course Name')),
                ('score', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Score')),
                ('pass_yr', models.IntegerField(choices=[(1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], verbose_name='Passing Year')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Job', models.CharField(max_length=20, verbose_name='Job Name')),
                ('start_yr', models.IntegerField(choices=[(1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], verbose_name='Starting Year')),
                ('designation', models.CharField(max_length=20, verbose_name='Designation')),
                ('add', models.TextField(blank=True, verbose_name='Additional')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('type', models.CharField(max_length=200, verbose_name='Industry')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Project name')),
                ('duration', models.IntegerField(verbose_name='Duration (yrs)')),
                ('version', models.CharField(max_length=15, verbose_name='Version')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Skill')),
                ('type', models.CharField(max_length=20, verbose_name='type')),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=20, verbose_name='Last Name')),
                ('Email', models.EmailField(max_length=254, verbose_name='Email')),
                ('LinkedIn', models.URLField(verbose_name='LinkedIn')),
                ('Ach', models.ManyToManyField(to='Resumer.Achievement')),
                ('address', models.ManyToManyField(to='Resumer.Addresse')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resumer.contact')),
                ('education', models.ManyToManyField(to='Resumer.Education')),
                ('exp', models.ManyToManyField(to='Resumer.Experience')),
                ('skills', models.ManyToManyField(to='Resumer.Skill')),
            ],
        ),
        migrations.AddField(
            model_name='experience',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resumer.organization'),
        ),
        migrations.AddField(
            model_name='experience',
            name='project',
            field=models.ManyToManyField(to='Resumer.Project'),
        ),
        migrations.AddField(
            model_name='education',
            name='institute',
            field=models.ManyToManyField(to='Resumer.Organization'),
        ),
    ]
