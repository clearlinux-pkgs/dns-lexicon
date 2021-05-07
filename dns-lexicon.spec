#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dns-lexicon
Version  : 3.6.0
Release  : 46
URL      : https://files.pythonhosted.org/packages/86/6e/33ebb9fa794440531c2eb96b3906e11f9ab5f9d85fd8c9f4342867770766/dns-lexicon-3.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/86/6e/33ebb9fa794440531c2eb96b3906e11f9ab5f9d85fd8c9f4342867770766/dns-lexicon-3.6.0.tar.gz
Summary  : Manipulate DNS records on various DNS providers in a standardized/agnostic way
Group    : Development/Tools
License  : MIT
Requires: dns-lexicon-bin = %{version}-%{release}
Requires: dns-lexicon-license = %{version}-%{release}
Requires: dns-lexicon-python = %{version}-%{release}
Requires: dns-lexicon-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
============
|logo_named|
============
Manipulate DNS records on various DNS providers in a standardized/agnostic way.

%package bin
Summary: bin components for the dns-lexicon package.
Group: Binaries
Requires: dns-lexicon-license = %{version}-%{release}

%description bin
bin components for the dns-lexicon package.


%package license
Summary: license components for the dns-lexicon package.
Group: Default

%description license
license components for the dns-lexicon package.


%package python
Summary: python components for the dns-lexicon package.
Group: Default
Requires: dns-lexicon-python3 = %{version}-%{release}

%description python
python components for the dns-lexicon package.


%package python3
Summary: python3 components for the dns-lexicon package.
Group: Default
Requires: python3-core
Provides: pypi(dns_lexicon)
Requires: pypi(beautifulsoup4)
Requires: pypi(cryptography)
Requires: pypi(pyyaml)
Requires: pypi(requests)
Requires: pypi(tldextract)

%description python3
python3 components for the dns-lexicon package.


%prep
%setup -q -n dns-lexicon-3.6.0
cd %{_builddir}/dns-lexicon-3.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619996186
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dns-lexicon
cp %{_builddir}/dns-lexicon-3.6.0/LICENSE %{buildroot}/usr/share/package-licenses/dns-lexicon/d7389b6482179505c25d9b209b006826fcb6b85c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lexicon

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dns-lexicon/d7389b6482179505c25d9b209b006826fcb6b85c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
