from .models import Category, Tag, Seller, Product


def setInitVal(category, tag, seller, product):
    c = Category.objects.get_or_create(name=category)
    t = Tag.objects.get_or_create(name=tag)
    s = Seller.objects.get_or_create(name=seller)
    p = Product.objects.get_or_create(name=product)


# use save method
# def setInitVal():
#     c = Category(name='laptop')
#     t = Tag(name='notebook')
#     s = Seller(name='acer corp')
#     p = Product(name='acer nitro 5')
#
#     c.save()
#     t.save()
#     s.save()
#     p.save()

# use create method
# def setInitVal():
#     c = Category.objects.create(name='laptop')
#     t = Tag.objects.create(name='notebook')
#     s = Seller.objects.create(name='acer corp')
#     p = Product.objects.create(name='acer nitro 5')


# setInitVal('laptop',
#            'notebook',
#            'acer corp',
#            'acer nitro 5')
# setInitVal('laptop',
#            'notebook',
#            'asus rog',
#            'asus corp')

# f = Product.objects.filter(name='acer nitro 5')


# def test():
#     setInitVal('laptop',
#                'notebook',
#                'acer nitro 5',
#                'acer corp')
#     setInitVal('laptop',
#                'notebook',
#                'asus corp',
#                'acer rog')
#     print(f)
