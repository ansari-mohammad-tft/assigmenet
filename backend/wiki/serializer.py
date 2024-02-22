import wikipedia
from rest_framework import serializers
from collections import Counter
import re
from .models import TopWordsModel


class TopWordsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopWordsModel
        fields = ['topic', 'n', 'top_words', 'created_at']
        read_only_fields = ['top_words', 'created_at']

    def create(self, validated_data):
        top_words = get_top_n_frequent_words(validated_data['topic'], validated_data['n'])
        validated_data['top_words'] = top_words
        return super().create(validated_data)


def get_top_n_frequent_words(topic, n):
    result = wikipedia.summary(topic, sentences=n)
    # Removing punctuation and converting to lowercase
    cleaned_text = re.sub(r'[^\w\s]', '', result.lower())

    # Counting word frequencies
    word_counts = Counter(cleaned_text.split())

    # Getting the top N frequent words
    top_words = [{"word": word, "count": count} for word, count in word_counts.most_common(n)]

    return top_words
