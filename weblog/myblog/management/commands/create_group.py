from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'This command is to create different groups and set permission for them.'

    def add_arguments(self, parser):
        parser.add_argument('group_name', type=str, choices=["author", "editor", "admin", "all"],
                            help='Use To create a group of users and set permissions for it.')
        parser.add_argument('--set', action='store_true', help='To set permission for an existing group.')

    def handle(self, *args, **options):
        author_perms = ["add_post", "change_post", "view_post", "add_comment", "view_comment",
                        "change_activation", "add_tag", "view_tag"]
        editor_perms = author_perms + ["can_confirm_posts", "change_comment", "can_confirm_comments",
                                       "change_all_activation"]
        admin_perms = editor_perms + ["add_user", "change_user", "view_user", "delete_user", "view_likepostlog",
                                      "view_likecommentlog", "add_userextrainfo", "change_userextrainfo",
                                      "delete_userextrainfo", "view_userextrainfo"]
        if options['group_name'] == 'author':
            new_group, created = Group.objects.get_or_create(name='نويسندگان')
            if created or options['set']:
                for i in author_perms:
                    new_group.permissions.add(Permission.objects.get(codename=i))
                if created:
                    self.stdout.write(self.style.SUCCESS('Author group created and permission has been set.'))
                else:
                    self.stdout.write(self.style.SUCCESS('Permissions has been set for "author".'))
            else:
                raise CommandError('Author group was created before!')

        elif options['group_name'] == 'editor':
            new_group, created = Group.objects.get_or_create(name='ويراستاران')
            if created or options['set']:
                for i in editor_perms:
                    new_group.permissions.add(Permission.objects.get(codename=i))
                if created:
                    self.stdout.write(self.style.SUCCESS('Editor group created and permission has been set.'))
                else:
                    self.stdout.write(self.style.SUCCESS('Permissions has been set for "editor".'))
            else:
                raise CommandError('Editor group was created before!')

        elif options['group_name'] == 'admin':
            new_group, created = Group.objects.get_or_create(name='مديران')
            if created or options['set']:
                for i in admin_perms:
                    new_group.permissions.add(Permission.objects.get(codename=i))
                if created:
                    self.stdout.write(self.style.SUCCESS('Admin group created and permission has been set.'))
                else:
                    self.stdout.write(self.style.SUCCESS('Permissions has been set for "admin".'))
            else:
                raise CommandError('Admin group was created before!')

        elif options['group_name'] == 'all':
            exist = list()
            new_group1, created1 = Group.objects.get_or_create(name='نويسندگان')
            new_group2, created2 = Group.objects.get_or_create(name='ويراستاران')
            new_group3, created3 = Group.objects.get_or_create(name='مديران')
            for i in [(new_group1, created1, author_perms), (new_group2, created2, editor_perms),
                      (new_group3, created3, admin_perms)]:
                try:
                    if i[1]:
                        for j in i[2]:
                            i[0].permissions.add(Permission.objects.get(codename=j))
                    else:
                        exist.append(i[0])
                        raise CommandError(f'{i[0]} group was created before!')
                except CommandError:
                    pass

            self.stdout.write(self.style.SUCCESS(f'{3 - len(exist)} group(s) created and permissions has been set.\n'
                                                 f'{exist} was created before!'))
