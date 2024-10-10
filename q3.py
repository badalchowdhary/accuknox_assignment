# Q3

# By default, Django signals run in the same database transaction as the caller, 
# but it depends on the signal type.


@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    def after_commit():
        print("Signal handler executed after transaction commit")

    transaction.on_commit(after_commit)

def create_user():
    print("Creating user...")
    user = User.objects.create(username='testuser')
    print("User created")

create_user()

# Output

# Creating user...
# User created
# Signal handler executed after transaction commit