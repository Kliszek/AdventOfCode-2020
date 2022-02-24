passports = []

lines = list()
elems = dict()

with open("input.txt", "r") as f:
    for line in f:
        lines.extend(line.strip(" \n").split(" "))
    for entry in lines:
        if entry == "":
            passports.append(elems)
            elems = dict()
        else:
            elems[entry.split(":")[0]] = entry.split(":")[1]
    if len(elems) > 0:
        passports.append(elems)

def is_valid(psprt):
    byr = range(1920, 2002+1)
    iyr = range(2010, 2020+1)
    eyr = range(2020, 2030+1)
    hgt = {"cm":range(150,193+1), "in":range(59,76+1)}
    hcl = "1234567890abcdef"
    ecl = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    #pid

    if (
                int(psprt["byr"]) in byr
            and int(psprt["iyr"]) in iyr
            and int(psprt["eyr"]) in eyr
            and psprt["hgt"][-2:] in hgt
                and int(psprt["hgt"][:-2]) in hgt[psprt["hgt"][-2:]]
            and psprt["hcl"][0] == "#"
                and not False in (s in hcl for s in psprt["hcl"][1:]) 
            and psprt["ecl"] in ecl
            and len(psprt["pid"]) == 9
                and psprt["pid"].isnumeric()
            ):
        return True
    return False


valid = 0
for psprt in passports:
    if ("byr" in psprt and "iyr" in psprt
            and "eyr" in psprt and "hgt" in psprt
            and "hcl" in psprt and "ecl" in psprt
            and "pid" in psprt):
        valid += bool(is_valid(psprt))



print(f"Valid passports: {valid}")
test = "abcf"
ll = ["a", "b", "c"]
print(test[1:])
print(   bool(not False in (s in ll for s in test))   )