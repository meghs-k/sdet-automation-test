def validate_image_size(width, height):
    errors = []

    if width <= 1000:
        errors.append(f"Image width is {width}; expected width > 1000")

    if height <= 1000:
        errors.append(f"Image height is {height}; expected height > 1000")

    return errors


'''The validate_image_size(width, height) function validates 
the image dimensions displayed on the third DuckDuckGo image result card.'''