from app import app
from models import db, User, Post, Group, user_group

with app.app_context():
    # Clear existing data
    User.query.delete()
    Post.query.delete()
    Group.query.delete()
    
    db.session.query(user_group).delete()
    db.session.commit()

    # Add new users
    u1 = User(username='user1', email='user1@example.com')
    u2 = User(username='user2', email='user2@example.com')
    u3 = User(username='user3', email='user3@example.com')
    u4 = User(username='user4', email='user4@example.com')
    u5 = User(username='user5', email='user5@example.com')

    db.session.add_all([u1, u2, u3, u4, u5])
    db.session.commit()

    # Add new posts
    p1 = Post(title='Post 1', content='post1 content', user=u1)
    p2 = Post(title='Post 2', content='post2 content', user=u1)
    p3 = Post(title='Post 3', content='post3 content', user=u1)
    p4 = Post(title='Post 4', content='post4 content', user=u2)
    p5 = Post(title='Post 5', content='post5 content', user=u1)
    p6 = Post(title='Post 6', content='post6 content', user=u3)
    p7 = Post(title='Post 7', content='post7 content', user=u1)
    p8 = Post(title='Post 8', content='post8 content', user=u5)
    p9 = Post(title='Post 9', content='post9 content', user=u4)
    p10 = Post(title='Post 10', content='post10 content', user=u2)

    db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])
    db.session.commit()

    # Add new groups
    g1 = Group(name='Group 1')
    g2 = Group(name='Group 2')
    g3 = Group(name='Group 3')
    g4 = Group(name='Group 4')
    g5 = Group(name='Group 5')

    db.session.add_all([g1, g2, g3, g4, g5])
    db.session.commit()

    # Add groups to users
    u1.groups.append(g5)
    u1.groups.append(g2)

    # Add users to groups
    g5.users.append(u2)
    g5.users.append(u5)
    g4.users.append(u3)
    g4.users.append(u1)

    db.session.commit()
