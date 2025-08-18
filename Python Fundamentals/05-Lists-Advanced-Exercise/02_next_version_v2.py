previous_version = input().split('.')

previous_version_as_integer = int(''.join(previous_version))
next_version_as_integer = previous_version_as_integer + 1
next_version = [digit for digit in str(next_version_as_integer)]

print('.'.join(next_version))