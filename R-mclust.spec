%global packname  mclust
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          4.2
Release:          1
Summary:          Model-Based Clustering / Normal Mixture Modeling
Group:            Sciences/Mathematics
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/mclust_4.2.tar.gz
Requires:         R-stats R-utils 
Requires:         R-mix 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-stats R-utils
BuildRequires:    R-mix 
BuildRequires:    blas-devel
BuildRequires:    lapack-devel

%description
Model-based clustering and normal mixture modeling including Bayesian

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
#%doc %{rlibdir}/%{packname}/cite
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
#%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/NEWS


%changelog
* Fri Feb 17 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.4.11-1
+ Revision: 775949
- Import R-mclust
- Import R-mclust



