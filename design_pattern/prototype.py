import copy
from os import O_NONBLOCK


class Website:
    def __init__(self, name, domain, desc, author, **kwargs):
        self.name = name
        self.domain = domain
        self.desc = desc
        self.authore = author

        for key in kwargs:
            setattr(self, key, kwargs.get(key, None))

    def __str__(self):
        summary = [
            f'Website "{self.name}"\n',
        ]

        infos = vars(self).items()
        ordered_infos = sorted(infos)

        for attr, val in ordered_infos:
            if attr == "name":
                continue
            summary.append(f"{attr}:{val} \n")
        return "".join(summary)


class Prototype:
    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attrs):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError
        obj = copy.deepcopy(found)
        for key in attrs:
            setattr(obj, key, attrs[key])

        return obj


def main():
    keywords = ("python", "data", "apis", "automation")
    site1 = Website(
        "ContentGardening",
        domain="contentgardening.com",
        desc="Automation and data-driven apps",
        author="Kamon Ayeva",
        category="Blog",
        keywords=keywords,
    )

    prototype = Prototype()
    identifier = "ka-cg-1"
    prototype.register(identifier, site1)

    site2 = prototype.clone(
        identifier,
        name="ContentGardeningPlayground",
        domain="play.contentgardening.com",
        desc="Experimentation for techniques featured on the blog",
        category="Membership site",
        creation_date="2018-08-01",
    )

    for site in (site1, site2):
        print(site)
    print(f"ID site1 : {id(site1)} != ID site2 : {id(site2)}")


if __name__ == "__main__":
    main()
