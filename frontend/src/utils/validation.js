export const validateEmailMethod = (email) => {
    return (/^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(email))
}

export const validatePasswordMethod = (password) => {
    const containsUppercase = /[A-Z]/.test(password)
    const containsLowercase = /[a-z]/.test(password)
    const containsNumber = /[0-9]/.test(password)
    const containsSpecial = /[#?!@$%^&*-]/.test(password)
    return containsUppercase && containsLowercase && containsNumber && containsSpecial && password.length >= 9
}

export const validateRepeatPasswordMethod = (password, repeatPassword) => {
    return (repeatPassword === password)
}
