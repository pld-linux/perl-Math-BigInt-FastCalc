#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	BigInt-FastCalc
Summary:	Math::BigInt::FastCalc - some XS to support Math::BigInt
Summary(pl):	Math::BigInt::FastCalc - XS wspieraj±ce Math::BigInt
Name:		perl-Math-BigInt-FastCalc
Version:	0.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	998a247a55bdc39c2a4906207d8ba247
Patch0:		%{name}-test.patch
BuildRequires:	perl-Math-BigInt >= 1.62
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Math-BigInt >= 1.62
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a replacement library for Math::BigInt::Calc that reimplements
some of the Calc functions in XS.

%description -l pl
Ten modu³ jest zamiennikiem Math::BigInt::Calc, bêd±cym
reimplementacj± czê¶ci funkcji Calc w XS.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
# sqrt(+inf) == inf, not NaN
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS README
%{perl_vendorarch}/Math/BigInt/FastCalc.pm
%dir %{perl_vendorarch}/auto/Math/BigInt/FastCalc
%{perl_vendorarch}/auto/Math/BigInt/FastCalc/FastCalc.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Math/BigInt/FastCalc/FastCalc.so
%{_mandir}/man3/*
