from django.core.management.base import BaseCommand

from faker import Faker
from django_seed import Seed

from quiz.models import Quiz



class Command(BaseCommand):
    model_name = f'{Quiz}'
    help = f'이 명령은 {Quiz}를 만듭니다'

    def handle(self, *args, **options):
        seeder = Seed.seeder()
        fake = Faker(['ko_KR'])

        quizs = [
            ['플러터의 대표적인 상태 관리 기법이 아닌것은?', 'vuex/setState()/Provider/BLoC', 0],
            ['플러터에 대한 설명으로 옳은 것은?', '인스타그램이 만든 것이다./알리바바 앱이 플러터로 만들어졌다./데스크탑 앱은 만들 수 없다./리엑트 네이티브 보다 성능이 않좋다.', 1],
            ['넷플릭스 클론 코딩 강의가 올라간 곳은?', '아프리카/트위치/인프런/넷플릭스', 2],
            ['플러터의 타입이 아닌 것은?', 'String/bool/int/Num', 3],
        ]

        for quiz in quizs:
            Quiz.objects.create(
                title=quiz[0],
                body=quiz[1],
                answer=quiz[2]
            )