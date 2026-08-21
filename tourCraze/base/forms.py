from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import CusUser, Post, Comment


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = CusUser
        fields = ["name", "username", "email", "password1", "password2"]


class UpdateUser(ModelForm):
    class Meta:
        model = CusUser
        fields = ["name", "avatar", "username", "email", "bio"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["content", "image"]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": "custom-content-input",
                    "placeholder": "Share your travel experience...",
                    "rows": 4,
                }
            ),
            "image": forms.ClearableFileInput(
                attrs={
                    "class": "custom-image-input",
                }
            ),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]


class TripPlanForm(forms.Form):
    STYLE_CHOICES = [
        ("Adventure", "Adventure 🧗"),
        ("Relaxed", "Relaxed 🌴"),
        ("Luxury", "Luxury ✨"),
        ("Budget", "Budget 🎒"),
        ("Family", "Family 👨‍👩‍👧‍👦"),
    ]

    INTEREST_CHOICES = [
        ("Food", "Food & Culinary 🍲"),
        ("Nature", "Nature & Outdoors 🌿"),
        ("History", "History & Culture 🏛️"),
        ("Shopping", "Shopping & Bazaars 🛍️"),
        ("Nightlife", "Nightlife & Music 🌙"),
        ("Photography", "Photography & Vistas 📸"),
        ("Wellness", "Wellness & Spa 🧘"),
    ]

    destination = forms.CharField(
        max_length=200,
        min_length=2,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg trip-input",
                "placeholder": "Where do you want to go? (e.g. Manali, Goa, Kashmir, Paris)",
                "autocomplete": "off",
            }
        ),
        error_messages={
            "required": "Please enter a destination to plan your trip.",
            "min_length": "Destination name must be at least 2 characters.",
        }
    )

    days = forms.IntegerField(
        min_value=1,
        max_value=14,
        initial=3,
        required=True,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control trip-input",
                "min": "1",
                "max": "14",
                "placeholder": "Days (1-14)",
            }
        ),
        error_messages={
            "min_value": "Trip duration must be at least 1 day.",
            "max_value": "Trip planner supports itineraries up to 14 days.",
        }
    )

    travelers = forms.IntegerField(
        min_value=1,
        max_value=20,
        initial=2,
        required=True,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control trip-input",
                "min": "1",
                "max": "20",
                "placeholder": "Travelers (1-20)",
            }
        ),
        error_messages={
            "min_value": "Number of travelers must be at least 1.",
            "max_value": "For groups larger than 20, please contact our group tour specialist.",
        }
    )

    budget = forms.IntegerField(
        min_value=1000,
        initial=25000,
        required=True,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control trip-input",
                "placeholder": "Approximate Budget in ₹",
                "min": "1000",
                "step": "500",
            }
        ),
        error_messages={
            "min_value": "Please specify an approximate budget of at least ₹1,000.",
        }
    )

    travel_style = forms.ChoiceField(
        choices=STYLE_CHOICES,
        initial="Relaxed",
        required=True,
        widget=forms.RadioSelect(
            attrs={
                "class": "btn-check",
            }
        )
    )

    interests = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control trip-input",
                "placeholder": "Food, Nature, History, Photography",
            }
        )
    )

    start_date = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                "class": "form-control trip-input",
                "type": "date",
            }
        )
    )

    def clean_destination(self):
        dest = self.cleaned_data.get("destination", "").strip()
        if len(dest) < 2:
            raise forms.ValidationError("Please provide a valid destination name.")
        return dest

    def clean_interests(self):
        val = self.cleaned_data.get("interests", "")
        if isinstance(val, list):
            return ", ".join(val)
        return str(val)
