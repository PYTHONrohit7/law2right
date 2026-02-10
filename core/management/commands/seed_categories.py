from django.core.management.base import BaseCommand
from django.utils.text import slugify
from core.models import Category

CATEGORIES = [
    "Indian Courts & Legal System",
    "Law Career & Education",
    "Law Exams & Preparation",
    "Core Law Subjects & Summaries",
    "Career & Opportunities in Law",
    "Legal Awareness & Simplified Acts",
    "Daily Legal News & Updates",
]

SLUG_OVERRIDES = {
    "Indian Courts & Legal System": "indian-courts-legal-system",
    "Law Career & Education": "law-career-education",
    "Law Exams & Preparation": "law-exams-preparation",
    "Core Law Subjects & Summaries": "core-law-subjects-summaries",
    "Career & Opportunities in Law": "career-opportunities-in-law",
    "Legal Awareness & Simplified Acts": "legal-awareness-simplified-acts",
    "Daily Legal News & Updates": "daily-legal-news-updates",
}

class Command(BaseCommand):
    help = "Seed the 7 required Law2Rights categories"

    def handle(self, *args, **options):
        created = 0
        for name in CATEGORIES:
            slug = SLUG_OVERRIDES.get(name, slugify(name))
            obj, was_created = Category.objects.get_or_create(slug=slug, defaults={'name': name})
            if was_created:
                created += 1
                self.stdout.write(self.style.SUCCESS(f"Created category: {name} ({slug})"))
            else:
                self.stdout.write(f"Exists: {name} ({slug})")
        self.stdout.write(self.style.SUCCESS(f"Seeding complete. {created} created."))
