from django.test import TestCase
from django.urls import reverse
from .models import Waiter
from .forms import SignupForm

class WaiterModelTests(TestCase):
    
    def test_rank(self):
        # test rank by creation date for waiters with the same score
        a = Waiter.create('apple')
        b = Waiter.create('banana')
        c = Waiter.create('cranberry')
        a.save()
        b.save()
        c.save()
        self.assertEqual(a.rank(), 1)
        self.assertEqual(b.rank(), 2)
        self.assertEqual(c.rank(), 3)

        # make sure adding referrals decreases rank
        c.increment_score()
        c.save()
        self.assertEqual(a.rank(), 2)
        self.assertEqual(b.rank(), 3)
        self.assertEqual(c.rank(), 1)


class WaitlistIndexTests(TestCase):
    
    def test_exists(self):
        response = self.client.get(reverse('waitlist:index'))
        self.assertEqual(response.status_code, 200)


class WaitlistJoinTests(TestCase):

    def test_join_without_referral(self):
        form = SignupForm(data={'username': 'apple'})
        response = self.client.post(
            reverse('waitlist:join'),
            form.data
        )
        self.assertEqual(response.status_code, 200)
        waiter = Waiter.objects.filter(username='apple').first()
        self.assertIsNotNone(waiter)

    def test_join_with_referral(self):
        form = SignupForm(data={'username': 'apple'})
        response = self.client.post(
            reverse('waitlist:join'),
            form.data
        )
        self.assertEqual(response.status_code, 200)
        a = Waiter.objects.filter(username='apple').first()
        self.assertIsNotNone(a)

        form = SignupForm(data={'username': 'banana', 'referrer': 'apple'})
        response = self.client.post(
            reverse('waitlist:join'),
            form.data
        )
        self.assertEqual(response.status_code, 200)
        b = Waiter.objects.filter(username='banana').first()
        self.assertIsNotNone(b)
        a = Waiter.objects.filter(username='apple').first()
        self.assertEqual(a.score, 1)

    # TODO: test joining with taken username
    # TODO: test joining with invalid referrer


class WaiterViewTests(TestCase):
    
    def test_display_rank(self):
        a = Waiter.create('apple')
        a.save()
        response = self.client.get(reverse('waitlist:get-waiter', args=(a.username,)))
        self.assertContains(response, "Your rank is")
        self.assertEqual(response.status_code, 200)


    def test_not_found(self):
        response = self.client.get(reverse('waitlist:get-waiter', args=('apple',)))
        self.assertEqual(response.status_code, 404)
