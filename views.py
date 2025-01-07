from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly,IsAdminUser
from rest_framework.decorators import api_view, APIView, permission_classes
from .models import Post
from .serializers import PostSerializer  # Ensure this matches your actual serializer name
from django.shortcuts import get_object_or_404
from .permissions import ReadOnly, AuthorOrReadOnly
from accounts.serializers import CurrentUserPostsSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

class CustomPaginator(PageNumberPagination):
    page_size = 3
    page_query_param='page'
    page_size_query_param='page_size'

@api_view(http_method_names=["GET","POST"])
def homepage(request: Request):
    if request.method == "POST":
        data = request.data
        response = {"message": "Hello World", "data": data}
        return Response(data=response, status=status.HTTP_201_CREATED)

    response = {"message": "Hello World"}
    return Response(data=response, status=status.HTTP_200_OK)

class PostListCreateView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class= PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPaginator
    queryset = Post.objects.all().order_by('-created')  # Order by created_at
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['created', 'title']  # Fields that can be used for ordering
    ordering = ['-created']  # Default ordering
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)
        return super().perform_create(serializer)
    @swagger_auto_schema(
        operation_summary="list all post",
        operation_description="this returns list of all posts"
    )
    def get (self, request:Request, *args, **kwargs):
       return self.list(request, *args, **kwargs) 
    @swagger_auto_schema(
        operation_summary="create a post",
        operation_description="this endpoint create a post"
    )
    def post(self, request:Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
class PostRetrieveUpdateDeleteView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PostSerializer
    permission_classes=[AuthorOrReadOnly]
    queryset=Post.objects.all()
    @swagger_auto_schema(
        operation_summary="retrive a post",
        operation_description="this endpoint will retrive a post"
    )
    def get(self, request:Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary="update a post",
        operation_description="this endpoint will update a post"
    )
    def put(self, request:Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary="delete a post",
        operation_description="this endpoint will delete a post"
    )
    def delete(self,request:Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

@api_view(http_method_names=["GET"])
@permission_classes([IsAuthenticated])
def get_posts_for_current_user(request: Request):
    user = request.user

    serializer = CurrentUserPostsSerializer(instance=user, context={"request": request})

    return Response(data=serializer.data, status=status.HTTP_200_OK)    
class ListPostsForAuthor(
    generics.GenericAPIView,
    mixins.ListModelMixin
):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        username = self.request.query_params.get("username") or None
        queryset = Post.objects.all()
        if username is not None:
            return Post.objects.filter(author__username=username)
        return queryset
    
    @swagger_auto_schema(
        operation_summary="list post for an author who is a user ",
        operation_description="this retrive a post by an id"
    )
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)