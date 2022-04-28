from dataclasses import field
from unicodedata import category
import graphene
from graphene_django import DjangoObjectType
from .models import Book, Category

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id','title')

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ('id','title','price','author','category','description','quantity','date_created')

class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    books = graphene.List(BookType)

    def resolve_books(root, info, **kwargs):
        return Book.objects.all()

    def resolve_categories(root, info, **kwargs):
        return Category.objects.all()

#schema = graphene.Schema(query=Query)


class CategoryInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()

class UpdateCategory(graphene.Mutation):
    class Arguments:
        # Mutation to update a category 
        title = graphene.String(required=True)
        id = graphene.ID()


    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, title, id):
        category = Category.objects.get(pk=id)
        category.title = title
        category.save()
        
        return UpdateCategory(category=category)

class CreateCategory(graphene.Mutation):
    class Arguments:
        # Mutation to create a category
        title = graphene.String(required=True)

    # Class attributes define the response of the mutation
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, title):
        category = Category()
        category.title = title
        category.save()
        
        return CreateCategory(category=category)

class BookInput(graphene.InputObjectType):
    title = graphene.String()
    category = graphene.Int()
    author = graphene.String()
    price = graphene.Int()
    quantity = graphene.Int()
    description = graphene.String()

class CreateBook(graphene.Mutation):
    class Arguments:
        input = BookInput(required=True)

    book = graphene.Field(BookType)
    
    @classmethod
    def mutate(cls, root, info, input):
        book = Book()
        #category_id = Category.objects.get(pk=input.category_id.id)
        book.title = input.title
        book.author = input.author
        #category.title = input.category
        book.category_id = input.category
        book.price = input.price
        book.quantity = input.quantity
        book.description = input.description
        book.save()
        return CreateBook(book=book)

class UpdateBook(graphene.Mutation):
    class Arguments:
        input = BookInput(required=True)
        id = graphene.ID()

    book = graphene.Field(BookType)
    
    @classmethod
    def mutate(cls, root, info, input, id):
        book = Book.objects.get(pk=id)
        book.title = input.title
        book.category_id = input.category
        book.author = input.author
        book.description = input.description
        book.price = input.price
        book.quantity = input.quantity
        book.save()
        return UpdateBook(book=book)

class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)