package companynames_test

import (
	"io/fs"
	"reflect"
	"testing"
	"testing/fstest"

	companynames "github.com/conradmugabe/simple_web_scapper/src"
)

type StubFailingFs struct {
}

func (s StubFailingFs) Open(name string) (fs.File, error) {
	return nil, fs.ErrNotExist
}

func TestCompanyNames(t *testing.T) {
	fs := fstest.MapFS{
		"companies.txt":         {Data: []byte("new vision")},
		"textile_companies.txt": {Data: []byte("new vision")},
	}

	names, err := companynames.NewCompanyFromFs(fs)

	if err != nil {
		t.Fatal(err)
	}

	if len(names) != len(fs) {
		t.Errorf("got %d names, wanted %d names", len(names), len(fs))
	}
}

func TestFailingCompanyNames(t *testing.T) {
	fs := StubFailingFs{}

	_, err := companynames.NewCompanyFromFs(fs)
	if err == nil {
		t.Fatal("expected an error")
	}
}

func TestNewCompanyNames(t *testing.T) {
	fs := fstest.MapFS{
		"companies.txt": {Data: []byte("new vision")},
	}
	companies, _ := companynames.NewCompanyFromFs(fs)

	got := companies[0]
	want := companynames.Company{Name: "new vision"}

	assertCompany(t, got, want)
}

func assertCompany(t *testing.T, got companynames.Company, want companynames.Company) {
	t.Helper()
	if !reflect.DeepEqual(got, want) {
		t.Errorf("got %+v, want %+v", got, want)
	}

}
