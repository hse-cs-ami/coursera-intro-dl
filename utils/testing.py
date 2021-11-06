import json

import requests


class Grader:

    def __init__(self, assignment_key, parts=()):
        self.submission_page = 'https://www.coursera.org/api/onDemandProgrammingScriptSubmissions.v1'
        self.assignment_key = assignment_key
        self.answers = {part: None for part in parts}

    def submit(self, email, token):
        submission = {
            'assignmentKey': self.assignment_key,
            'submitterEmail': email,
            'secret': token,
            'parts': {}
        }
        for part, output in self.answers.items():
            if output is not None:
                submission['parts'][part] = {
                    'output': output
                }
            else:
                submission['parts'][part] = dict()

        request = requests.post(self.submission_page, data=json.dumps(submission))
        response = request.json()
        if request.status_code == 201:
            print('Submitted to Coursera platform. See results on assignment page!')
        elif u'details' in response and u'learnerMessage' in response[u'details']:
            print(response[u'details'][u'learnerMessage'])
        else:
            print('Unknown response from Coursera: {}'.format(request.status_code))
            print(response)

    def set_answer(self, part, answer):
        if isinstance(answer, str):
            self.answers[part] = answer
        else:
            try:
                self.answers[part] = ' '.join(map(repr, answer))
            except TypeError:
                self.answers[part] = repr(answer)


class Tester:

    def __init__(self, assignment_key, parts=()):
        self.grader: Grader = Grader(assignment_key=assignment_key, parts=parts)
        self.email: str = ''
        self.token: str = ''
        self.parts = parts

    def set_email(self, email: str):
        self.email = email

    def set_token(self, token: str):
        self.token = token


class TestWeek01(Tester):
    pass


class TestWeek02(Tester):

    def submit_wrapper(self, wrapper, part_idx):
        answer = [
            wrapper.history['test_accuracy'][-1].item(),
            wrapper.history['train_accuracy'][-1].item(),
            wrapper.history['test_loss'][-1].item(),
            wrapper.history['train_loss'][-1].item(),
        ]
        self.grader.set_answer(self.parts[part_idx], answer)
        self.grader.submit(self.email, self.token)

    def test01(self, wrapper):
        self.submit_wrapper(wrapper, 0)

    def test02(self, wrapper):
        self.submit_wrapper(wrapper, 1)

    def test03(self, wrapper):
        self.submit_wrapper(wrapper, 2)

    def test04(self, wrapper):
        self.submit_wrapper(wrapper, 3)


class TestWeek03(Tester):

    def test01(self, dataset_class):
        dataset = dataset_class()
        answer = [
            dataset[0][0].size,
            dataset[0][1].item()
        ]
        self.grader.set_answer(self.parts[0], answer)
        self.grader.submit(self.email, self.token)

    def test02(self, model):
        answer = [
            model.model.fc.in_features,
            model.model.fc.out_features
        ]
        self.grader.set_answer(self.parts[1], answer)
        self.grader.submit(self.email, self.token)

    def test03(self, wrapper):
        answer = [
            wrapper.history['test_accuracy'][-1].item(),
            wrapper.history['train_accuracy'][-1].item(),
            wrapper.history['test_loss'][-1].item(),
            wrapper.history['train_loss'][-1].item(),
        ]
        self.grader.set_answer(self.parts[2], answer)
        self.grader.submit(self.email, self.token)


class TestWeek04(Tester):
    pass


class TestWeek05(Tester):
    pass


class TestWeek06(Tester):
    pass
