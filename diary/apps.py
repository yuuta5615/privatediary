from django.apps import AppConfig
#アプリケーションを生成すると勝手にできてるから自分で作る必要ない

class DiaryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'diary'
