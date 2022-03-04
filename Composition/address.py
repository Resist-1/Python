class AddressClass:
    def __init__(self,Street1,LiveinCity,LiveinState,PostalCode,Country,Street2 = '' ):
        self.Street1 = Street1
        self.Street2 = Street2
        self.LiveinCity = LiveinCity
        self.LiveinState = LiveinState
        self.PostalCode = PostalCode
        self.Country = Country
    def __str__(self):
        totalLines = [self.Street1]
        if self.Street2:
            lines.append(self.Street2)
        totalLines.append(f'{self.LiveinCity}, {self.LiveinState} {self.PostalCode} {self.Country}')
        return '\n'.join(totalLines)