from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"


def unique_koala_facts(amount_of_facts):
    limit = 1000
    list_of_facts = []

    i = 0
    while i < limit:
        fact = random_koala_fact()

        if fact not in list_of_facts:
            list_of_facts.append(fact)
            if len(list_of_facts) == amount_of_facts:
                break

        i += 1

    # print(len(list_of_facts))
    return list_of_facts


def num_joey_facts():
    def set_bench_fact(random_koala_fact):
        koala_fact = random_koala_fact
        if "joey" not in koala_fact.lower() or "joey's" not in koala_fact:
            return random_koala_fact

    bench_fact = set_bench_fact(random_koala_fact())
    joey_facts = []
    bench_fact_count = 1

    while bench_fact_count <= 10:
        koala_fact = random_koala_fact()
        if koala_fact in bench_fact:
            bench_fact_count += 1
        elif "joey" in koala_fact.lower() or "joey's" in koala_fact.lower():
            if koala_fact not in joey_facts:
                joey_facts.append(koala_fact)
        else:

            continue

    return len(joey_facts)


def koala_weight():
    weight_in_kg = ""
    weight_found = False
    while weight_found == False:
        koala_fact = random_koala_fact()
        if "weigh" in koala_fact and "kg" in koala_fact:
            weight = koala_fact
            weight_found = True

    weight = weight[weight.find("weigh"):]
    for letter in weight:
        if letter.isdigit():
            weight_in_kg += letter

    return int(weight_in_kg)


# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    # print(random_koala_fact())
    print(unique_koala_facts(20))
    print(num_joey_facts())
    print(koala_weight())
