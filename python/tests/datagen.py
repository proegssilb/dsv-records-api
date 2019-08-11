import faker as f
import tests.userprovider


def make_faker(seed):
    faker_to_return = f.Faker()
    faker_to_return.seed_instance(seed)
    faker_to_return.add_provider(tests.userprovider.Provider)
    return faker_to_return
