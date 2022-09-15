from django import forms

class InquiryForm(forms.Form):
    name = forms.CharField(label = 'お名前', max_length = 30)
    age = forms.CharField(label='年齢', widget=forms.NumberInput)
    email = forms.EmailField(label = 'メールアドレス')
    title = forms.CharField(label = 'タイトル', max_length = 30)
    message = forms.CharField(label = 'メッセージ', widget = forms.Textarea)
    sns = forms.URLField(label = 'インスタ', widget = forms.URLInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前をここに入力してください'

        self.fields['age'].widget.attrs['class'] = 'form-control'
        self.fields['age'].widget.attrs['placeholder'] = '年齢を入力してください'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスをここに入力してください'

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルをここに入力してください'

        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージをここに入力してください'

        self.fields['sns'].widget.attrs['class'] = 'form-control'
        self.fields['sns'].widget.attrs['placeholder'] = 'ご自身のインスタグラムをここに入力してください'