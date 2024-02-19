package companynames

import (
	"io"
	"io/fs"
)

type Company struct {
	Name string
}

func NewCompanyFromFs(fileSystem fs.FS) ([]Company, error) {
	dir, err := fs.ReadDir(fileSystem, ".")
	if err != nil {
		return nil, err
	}
	var companies []Company
	for _, f := range dir {
		company, err := getCompany(fileSystem, f.Name())
		if err != nil {
			return nil, err
		}
		companies = append(companies, company)
	}
	return companies, nil
}

func getCompany(fileSystem fs.FS, fileName string) (Company, error) {
	companyFile, error := fileSystem.Open(fileName)
	if error != nil {
		return Company{}, error
	}
	defer companyFile.Close()
	return newCompany(companyFile)
}

func newCompany(companyFile io.Reader) (Company, error) {
	companyData, err := io.ReadAll(companyFile)
	if err != nil {
		return Company{}, err
	}
	company := Company{Name: string(companyData)[0:]}
	return company, nil
}
