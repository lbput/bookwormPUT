from oscar.apps.partner import strategy


class Selector(object):

    def strategy(self, request=None, user=None, **kwargs):
        return strategy.PL(request)

		
