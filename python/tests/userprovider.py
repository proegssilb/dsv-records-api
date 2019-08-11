import datetime as dt
from faker.providers.person import Provider as PersonProvider
from recordslib import User


colors = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'gold', 'silver', 'bronze', 'turquoise')


class Provider(PersonProvider):

    def user(self):
        is_male = self.random_int(0, 1)
        result = User()
        result.favorite_color = self.random_element(colors)
        result.birth_date = dt.date(self.random_int(1930, 2040), self.random_int(1, 12), self.random_int(1, 28))

        # This is not the proper way to handle gender, but it gets the point across, and the API is strange.
        if is_male:
            result.gender = 'Male'
            result.first_name = self.first_name_male()
            result.last_name = self.last_name_male()
        else:
            result.gender = 'Female'
            result.first_name = self.first_name_female()
            result.last_name = self.last_name_female()

        return result
