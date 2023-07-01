from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    post_id = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
            'id', 'user',
            'post', 'content'
        ]
    
    def get_amount_comments(self, obj):
        return obj.post_id.count()