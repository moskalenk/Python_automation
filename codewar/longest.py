def count_smileys(arr):

    count = 0
    for eye in eyes:
        for nose in noses:
            for mouth in mouths:
                face = eye + nose + mouth
                count += arr.count(face)
    return count

count_smileys([':D',':~)',';~D',':)'])